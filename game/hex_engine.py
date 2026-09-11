"""Reference implementation of a 3x3 Hex game.

The browser game mirrors these rules. A player wins only by creating a
connected component between their two opposite board edges.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from random import Random

EMPTY, BLUE, YELLOW = 0, 1, 2

DIRECTIONS = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0))


@dataclass
class HexGame:
    size: int = 3
    rng: Random = field(default_factory=Random)
    board: list[int] = field(init=False)
    current_player: int = field(default=BLUE, init=False)
    winner: int = field(default=EMPTY, init=False)
    winning_path: list[int] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        if self.size < 1:
            raise ValueError("size must be positive")
        self.board = [EMPTY] * (self.size * self.size)

    def index(self, row: int, col: int) -> int:
        return row * self.size + col

    def coordinates(self, index: int) -> tuple[int, int]:
        return divmod(index, self.size)

    def neighbors(self, index: int):
        row, col = self.coordinates(index)
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                yield self.index(nr, nc)

    def play(self, index: int) -> bool:
        if self.winner:
            return False
        if not 0 <= index < len(self.board) or self.board[index] != EMPTY:
            return False
        self.board[index] = self.current_player
        player = self.current_player
        path = self._find_path(player)
        if path:
            self.winner = player
            self.winning_path = path
        else:
            self.current_player = YELLOW if player == BLUE else BLUE
        return True

    def computer_move(self) -> int | None:
        if self.winner or self.current_player != YELLOW:
            return None
        choices = [i for i, value in enumerate(self.board) if value == EMPTY]
        if not choices:
            return None
        move = self.rng.choice(choices)
        self.play(move)
        return move

    def _find_path(self, player: int) -> list[int] | None:
        starts = (
            [self.index(r, 0) for r in range(self.size)]
            if player == BLUE
            else [self.index(0, c) for c in range(self.size)]
        )
        targets = (
            {self.index(r, self.size - 1) for r in range(self.size)}
            if player == BLUE
            else {self.index(self.size - 1, c) for c in range(self.size)}
        )
        starts = [i for i in starts if self.board[i] == player]
        queue = deque(starts)
        parent: dict[int, int | None] = {i: None for i in starts}
        while queue:
            current = queue.popleft()
            if current in targets:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return list(reversed(path))
            for neighbor in self.neighbors(current):
                if self.board[neighbor] == player and neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)
        return None

    def reset(self) -> None:
        self.board = [EMPTY] * (self.size * self.size)
        self.current_player = BLUE
        self.winner = EMPTY
        self.winning_path = []
