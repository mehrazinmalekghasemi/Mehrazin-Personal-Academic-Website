const theme=document.getElementById('theme');if(theme)theme.addEventListener('click',()=>document.body.classList.toggle('dark'));
const lang=document.getElementById('lang');
if(!lang){const b=document.createElement('button');b.className='floating-lang';b.id='lang';b.textContent='FR';b.setAttribute('aria-label','Switch language');Object.assign(b.style,{position:'fixed',top:'20px',right:'24px',zIndex:'100',border:'1px solid #ddd9f2',background:'#fffdfd',color:'#30305b',borderRadius:'999px',height:'34px',padding:'0 12px',cursor:'pointer',font:'10px "DM Mono"'});document.body.appendChild(b)}
const langButton=document.getElementById('lang');
function setLanguage(value){document.documentElement.lang=value;document.querySelectorAll('[data-en][data-fr]').forEach(el=>{el.innerHTML=el.dataset[value]});langButton.textContent=value==='en'?'FR':'EN';localStorage.setItem('site-language',value)}
langButton.addEventListener('click',()=>setLanguage((document.documentElement.lang||'en')==='en'?'fr':'en'));
const saved=localStorage.getItem('site-language')||'en';setLanguage(saved);
const year=document.getElementById('year');if(year)year.textContent=new Date().getFullYear();
document.querySelectorAll('.research-card').forEach(card=>{card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();card.style.transform=`perspective(700px) rotateX(${-(e.clientY-r.top-r.height/2)/35}deg) rotateY(${(e.clientX-r.left-r.width/2)/35}deg) translateY(-4px)`});card.addEventListener('mouseleave',()=>card.style.transform='')});