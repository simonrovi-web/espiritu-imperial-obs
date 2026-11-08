#!/usr/bin/env python3
"""Gráficos del evento "Espíritu Imperial" para OBS (carpeta out/): pantallas completas y overlays.
Dirección: premiación de gala televisiva con la marca Imperial (azul marino, rojo, blanco; Roboto Condensed)."""
import base64, io, os
from PIL import Image

B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = 'node_modules/@fontsource/'
def face(fam, path, w):
    return '@font-face{font-family:"%s";font-weight:%d;font-display:block;src:url(data:font/woff2;base64,%s) format("woff2");}' % (fam, w, B(F + path))
FONTS = ''.join([
    face('Roboto Condensed', 'roboto-condensed/files/roboto-condensed-latin-400-normal.woff2', 400),
    face('Roboto Condensed', 'roboto-condensed/files/roboto-condensed-latin-700-normal.woff2', 700),
    face('Roboto Condensed', 'roboto-condensed/files/roboto-condensed-latin-900-normal.woff2', 900),
    face('Roboto', 'roboto/files/roboto-latin-400-normal.woff2', 400),
    face('Roboto', 'roboto/files/roboto-latin-500-normal.woff2', 500),
])

def png(path, w):
    im = Image.open(path); im.thumbnail((w, w * 3), Image.LANCZOS); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
# El sitio solo publica el logo blanco en 300×81: se usa a 300 px o menos (nunca ampliado).
LOGO = png('../Logo_Imperial_web.png', 300)

# ---------------------------------------------------------------------------------------------
# Marca tomada de imperial.cl: azul marino #063661 / #003C69 / #163B66, rojo #ED2939 / #FF464B,
# grises #313131 y #85909E; Roboto Condensed (títulos) y Roboto (texto).
# ---------------------------------------------------------------------------------------------
BASE = r'''
:root{--nv:#063661;--nv2:#003C69;--nv3:#163B66;--dk:#041F3D;--dk2:#03152B;--rd:#ED2939;--rd2:#C8102E;--rdl:#FF464B;
 --wh:#FFFFFF;--mu:#AFC0D6;--gr:#85909E;--ink:#0E1B2C}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;font-family:"Roboto",sans-serif;color:var(--wh)}
.cd{font-family:"Roboto Condensed",sans-serif}
@keyframes up{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
@keyframes left{from{opacity:0;transform:translateX(-70px)}to{opacity:1;transform:none}}
@keyframes rise{from{opacity:0;transform:translateY(60px) scale(.97);filter:blur(8px)}to{opacity:1;transform:none;filter:none}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes sway{0%,100%{transform:rotate(-7deg)}50%{transform:rotate(7deg)}}
@keyframes sway2{0%,100%{transform:rotate(8deg)}50%{transform:rotate(-6deg)}}
@keyframes sweep{from{transform:translateX(-120%) skewX(-18deg)}to{transform:translateX(320%) skewX(-18deg)}}
@keyframes pulse{50%{opacity:.35}}
.hide{display:none!important}
'''
FULL = r'''
body{background:var(--dk)}
.stage{position:relative;width:1920px;height:1080px;overflow:hidden;
 background:radial-gradient(1300px 760px at 50% -14%,rgba(92,146,214,.42),transparent 62%),radial-gradient(1100px 420px at 50% 112%,rgba(237,41,57,.20),transparent 70%),linear-gradient(180deg,#0A2F5E 0%,#063661 38%,#041F3D 100%)}
.beam{position:absolute;top:-140px;width:520px;height:1500px;transform-origin:50% 0;pointer-events:none;
 background:linear-gradient(180deg,rgba(214,231,255,.20),rgba(214,231,255,.05) 55%,transparent 80%);clip-path:polygon(44% 0,56% 0,100% 100%,0 100%);mix-blend-mode:screen}
.beam.a{left:300px;animation:sway 14s ease-in-out infinite}
.beam.b{right:300px;animation:sway2 17s ease-in-out infinite}
.beam.c{left:700px;opacity:.6;animation:sway 21s ease-in-out infinite reverse}
.floor{position:absolute;left:0;right:0;bottom:120px;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.28) 30%,rgba(255,255,255,.28) 70%,transparent)}
.vig{position:absolute;inset:0;background:radial-gradient(1500px 900px at 50% 45%,transparent 55%,rgba(2,10,24,.55));pointer-events:none}
.logo{position:absolute;top:56px;left:80px;width:260px;z-index:4}
.bar{position:absolute;left:0;right:0;bottom:0;height:120px;background:rgba(3,21,43,.92);border-top:4px solid var(--rd);display:flex;align-items:center;padding:0 80px;z-index:4}
.cell{display:flex;align-items:center;gap:18px;padding:0 44px;border-left:1px solid rgba(255,255,255,.18);height:60px}
.cell:first-child{padding-left:0;border-left:0}
.cell svg{width:38px;height:38px;flex:none;stroke:var(--rdl);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.cell b{display:block;font-family:"Roboto Condensed";font-size:30px;font-weight:700;line-height:1.05;white-space:nowrap;text-transform:uppercase}
.cell span{display:block;font-size:22px;color:var(--mu);white-space:nowrap}
.cell.web{margin-left:auto;border-left:0;padding-right:0}
.kick{display:inline-flex;align-items:center;gap:14px;font-family:"Roboto Condensed";font-weight:700;font-size:30px;letter-spacing:4px;text-transform:uppercase;color:var(--wh)}
.kick::before{content:"";width:56px;height:6px;background:var(--rd);border-radius:3px}
.rule{width:140px;height:8px;background:var(--rd);border-radius:4px;transform-origin:left;animation:grow .7s .35s cubic-bezier(.16,1,.3,1) both}
'''

I_CAL = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24"><path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
I_WEB = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>'
BAR = ('<div class="bar"><div class="cell">' + I_CAL + '<div><b data-ev="fecha">FECHA DEL EVENTO</b><span data-ev="hora_txt">Inicio 19:00 h</span></div></div>'
       '<div class="cell">' + I_PIN + '<div><b data-ev="lugar">LUGAR</b><span data-ev="dir">Dirección, ciudad</span></div></div>'
       '<div class="cell web">' + I_WEB + '<div><b data-ev="web">imperial.cl</b><span data-ev="hashtag">#EspírituImperial</span></div></div></div>')
BG = '<div class="beam a"></div><div class="beam b"></div><div class="beam c"></div><div class="floor"></div><div class="vig"></div>'

LIVE = r'''
function fitEl(el){var mx=+el.dataset.max,mn=+el.dataset.min||20,f=mx;el.style.fontSize=f+'px';
 var over=el.dataset.fit==='h'?function(){return el.scrollHeight>el.clientHeight+4}:function(){return el.scrollWidth>el.clientWidth+1};
 while(over()&&f>mn){f-=2;el.style.fontSize=f+'px'}}
function fitAll(){document.querySelectorAll('[data-fit]').forEach(fitEl)}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function setT(sel,v){document.querySelectorAll(sel).forEach(function(el){if(v!=null&&el.textContent!==String(v))el.textContent=v})}
function ini(n){var w=(n||'').trim().split(/\s+/).filter(Boolean);return (((w[0]||'')[0]||'')+((w.length>1?w[w.length-1]:'')[0]||'')).toUpperCase()}
function anos(a){a=String(a||'').trim();if(!a)return '';return /^\d+$/.test(a)?a+(a==='1'?' año':' años')+' en Imperial':a}
var LAST=0,D={};
function applyLive(d){if(!d||!d.ts||d.ts<LAST)return;LAST=d.ts;D=d;
 if(d.ev){for(var k in d.ev)setT('[data-ev="'+k+'"]',d.ev[k]);document.querySelectorAll('[data-evshow]').forEach(function(e){e.classList.toggle('hide',!(d.ev[e.dataset.evshow]||'').trim())})}
 if(window.onLive)window.onLive(d);fitAll()}
window.addEventListener('imp',function(e){applyLive(e.detail)});
try{new BroadcastChannel('imp').onmessage=function(e){applyLive(e.data)}}catch(e){}
window.addEventListener('storage',function(e){if(e.key==='imp-live')try{applyLive(JSON.parse(e.newValue))}catch(x){}});
try{var L0=JSON.parse(localStorage.getItem('imp-live')||'null');if(L0)applyLive(L0)}catch(e){}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitAll);setTimeout(fitAll,300);
var Q=new URLSearchParams(location.search);
'''

def page(title, css, body, js='', full=True):
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>' + title + '</title><style>' + FONTS + BASE +
            (FULL if full else 'html,body{background:transparent}') + css + '</style></head><body>' + body +
            '<script>' + LIVE + js + '</script></body></html>')

P = {}

# =========================================================== INICIO
P['IMP_Inicio'] = page('Espíritu Imperial · Inicio', r'''
.c{position:absolute;left:0;right:0;top:250px;text-align:center;display:flex;flex-direction:column;align-items:center}
.k1{font-family:"Roboto Condensed";font-weight:400;font-size:64px;letter-spacing:22px;text-transform:uppercase;color:var(--mu);margin-right:-22px;animation:up .9s .1s ease both}
.k2{font-family:"Roboto Condensed";font-weight:900;font-size:220px;line-height:.86;letter-spacing:-2px;text-transform:uppercase;animation:rise 1.1s .25s cubic-bezier(.16,1,.3,1) both;position:relative;overflow:hidden;padding:0 20px}
.k2::after{content:"";position:absolute;top:0;bottom:0;width:180px;left:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);animation:sweep 1.6s 1.4s ease-in-out both}
.c .rule{margin:34px auto 0;transform-origin:center}
.lema{font-size:40px;color:var(--wh);margin-top:28px;animation:up .9s .45s ease both}
.cdw{margin-top:46px;display:inline-flex;align-items:center;gap:26px;background:rgba(3,21,43,.65);border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:14px 18px 14px 40px;animation:up .9s .6s ease both}
.cdw small{font-family:"Roboto Condensed";font-size:28px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--mu)}
.cdw b{font-family:"Roboto Condensed";font-size:64px;font-weight:900;line-height:1;font-variant-numeric:tabular-nums;background:var(--rd2);border-radius:999px;padding:8px 34px 10px}
.cdw b.soon{font-size:40px}
''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="c"><div class="k1" id="k1">Espíritu</div><div class="k2" id="k2">Imperial</div><div class="rule"></div>'
 + '<div class="lema" data-ev="lema" data-evshow="lema">Reconocemos a quienes hacen grande cada sucursal</div>'
 + '<div class="cdw"><small id="cdl">Comenzamos en</small><b id="cd">10:00</b></div></div>'
 + BAR + '</div>', r'''
var TGT=null;
window.onLive=function(d){if(d.ini){TGT=d.ini.target||null;if(d.ini.label)document.getElementById('cdl').textContent=d.ini.label}tick()};
function tick(){var b=document.getElementById('cd');var hora=(D.ev&&D.ev.hora)||'';
 if(!TGT){b.textContent=hora||'Pronto';b.classList.toggle('soon',!hora);return}
 var r=Math.max(0,Math.round((TGT-Date.now())/1000));b.classList.remove('soon');
 b.textContent=r>=3600?Math.floor(r/3600)+':'+String(Math.floor(r%3600/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0'):String(Math.floor(r/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0');
 if(r<=0){b.textContent='¡Comenzamos!';b.classList.add('soon')}}
setInterval(tick,250);tick();''')

# =========================================================== SUCURSAL (presenta la sucursal antes de su destacado)
P['IMP_Sucursal'] = page('Espíritu Imperial · Sucursal', r'''
.c{position:absolute;left:0;right:0;top:300px;text-align:center;display:flex;flex-direction:column;align-items:center}
.n{font-family:"Roboto Condensed";font-weight:700;font-size:30px;letter-spacing:4px;color:var(--mu);text-transform:uppercase;animation:up .8s ease both}
.c .kick{margin-top:18px;animation:up .8s .1s ease both}
.s{font-family:"Roboto Condensed";font-weight:900;font-size:200px;line-height:.9;text-transform:uppercase;letter-spacing:-1px;max-width:1700px;height:190px;display:flex;align-items:center;justify-content:center;white-space:nowrap;margin-top:24px;animation:rise 1s .2s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin:34px auto 0;transform-origin:center}
.z{font-size:44px;margin-top:28px;color:var(--wh);animation:up .8s .45s ease both}
''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="c"><div class="n" id="sn">Sucursal 1 de 12</div><div class="kick">Sucursal</div><div class="s" id="ss" data-fit="w" data-max="200" data-min="90">Nombre sucursal</div><div class="rule"></div><div class="z" id="sz">Ciudad</div></div>'
 + BAR + '</div>', r'''
window.onLive=function(d){var a=d.ag||{},L=a.items||[],c=a.cur||0,it=L[c]||{};
 document.getElementById('ss').textContent=it.t||'Sucursal';document.getElementById('sz').textContent=it.e||'';
 document.getElementById('sn').textContent=L.length?'Sucursal '+(c+1)+' de '+L.length:''};''')

# =========================================================== DESTACADO (revelación del trabajador)
P['IMP_Destacado'] = page('Espíritu Imperial · Destacado', r'''
.ph{position:absolute;left:150px;top:190px;width:560px;height:700px;border-radius:24px;overflow:hidden;background:linear-gradient(160deg,#163B66,#041F3D);box-shadow:0 40px 90px rgba(0,0,0,.5);animation:rise 1s .1s cubic-bezier(.16,1,.3,1) both}
.ph::before{content:"";position:absolute;inset:0;border-radius:24px;box-shadow:inset 0 0 0 2px rgba(255,255,255,.22);z-index:2;pointer-events:none}
.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ph .ini{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:"Roboto Condensed";font-weight:900;font-size:230px;color:rgba(255,255,255,.92)}
.ph .tag{position:absolute;left:0;right:0;bottom:0;z-index:3;background:linear-gradient(0deg,rgba(3,21,43,.92),transparent);padding:80px 34px 28px;font-family:"Roboto Condensed";font-weight:700;font-size:30px;letter-spacing:2px;text-transform:uppercase}
.ph .tag i{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--rd);margin-right:12px;vertical-align:3px}
.info{position:absolute;left:800px;top:230px;width:1000px}
.info .kick{animation:left .8s .3s ease both}
.nm{font-family:"Roboto Condensed";font-weight:900;font-size:132px;line-height:.92;text-transform:uppercase;margin-top:26px;height:250px;display:flex;align-items:flex-end;animation:rise 1s .45s cubic-bezier(.16,1,.3,1) both}
.info .rule{margin-top:30px;animation-delay:.8s}
.cg{font-size:44px;font-weight:500;margin-top:26px;animation:left .8s .7s ease both}
.meta{display:flex;gap:16px;margin-top:22px;animation:left .8s .82s ease both}
.meta span{font-family:"Roboto Condensed";font-weight:700;font-size:30px;padding:10px 26px;border-radius:999px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);white-space:nowrap}
.meta span.r{background:var(--rd2);border-color:var(--rd2)}
.mot{font-size:34px;line-height:1.35;color:var(--wh);margin-top:36px;max-width:960px;max-height:140px;overflow:hidden;padding-left:28px;border-left:4px solid rgba(255,255,255,.35);animation:up .8s 1s ease both}
''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="ph"><img id="dph" class="hide" alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="><div class="ini" id="din">NA</div><div class="tag"><i></i><span id="dsu">Sucursal</span></div></div>'
 + '<div class="info"><div class="kick" id="dk">Trabajador destacado</div>'
 + '<div class="nm" id="dnm" data-fit="h" data-max="132" data-min="70">Nombre Apellido</div><div class="rule"></div>'
 + '<div class="cg" id="dcg">Cargo</div><div class="meta"><span class="r" id="dms">Sucursal</span><span id="dma">Años en Imperial</span></div>'
 + '<div class="mot" id="dmo"></div></div>'
 + BAR + '</div>', r'''
var K='';
window.onLive=function(d){var o=d.ora||{},k=JSON.stringify([o.o,o.t,o.c,o.h,o.m,(o.foto||'').length,o.kicker]);if(k===K)return;K=k;
 document.getElementById('dk').textContent=o.kicker||'Trabajador destacado';
 document.getElementById('dnm').textContent=o.o||'Nombre Apellido';document.getElementById('din').textContent=ini(o.o)||'·';
 document.getElementById('dcg').textContent=o.c||'';document.getElementById('dsu').textContent=o.t?('Sucursal '+o.t):'';
 document.getElementById('dms').textContent=o.t||'';document.getElementById('dms').classList.toggle('hide',!o.t);
 document.getElementById('dma').textContent=anos(o.h);document.getElementById('dma').classList.toggle('hide',!o.h);
 var mo=document.getElementById('dmo');mo.textContent=o.m?('“'+o.m+'”'):'';mo.classList.toggle('hide',!o.m);
 var ph=document.getElementById('dph');if(o.foto){ph.src=o.foto;ph.classList.remove('hide');document.getElementById('din').classList.add('hide')}else{ph.classList.add('hide');document.getElementById('din').classList.remove('hide')}
 document.querySelectorAll('.ph,.nm,.cg,.meta,.mot,.kick,.rule').forEach(function(e){e.style.animation='none';void e.offsetWidth;e.style.animation=''})};''')

# =========================================================== DESTACADOS (tablero de todas las sucursales)
P['IMP_Destacados'] = page('Espíritu Imperial · Destacados', r'''
.hd{position:absolute;left:80px;top:150px;right:80px;display:flex;align-items:flex-end;justify-content:space-between}
.hd b{font-family:"Roboto Condensed";font-weight:900;font-size:96px;line-height:.9;text-transform:uppercase}
.hd span{font-size:30px;color:var(--mu);padding-bottom:6px}
.gr{position:absolute;left:80px;right:80px;top:300px;display:grid;grid-template-columns:repeat(var(--cols,4),minmax(0,1fr));gap:20px}
.it{position:relative;height:var(--h,148px);border-radius:16px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);padding:20px 24px;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;animation:up .6s ease both}
.it .s{font-family:"Roboto Condensed";font-weight:700;font-size:26px;letter-spacing:1.5px;text-transform:uppercase;color:var(--mu);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.it .n{font-family:"Roboto Condensed";font-weight:900;font-size:46px;line-height:1;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.it .c{font-size:22px;color:var(--mu);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.it.fut .n{color:rgba(255,255,255,.35)}
.it.cur{background:var(--wh);border:4px solid var(--rd);color:var(--ink);box-shadow:0 24px 60px rgba(0,0,0,.45)}
.it.cur .s{color:var(--rd2)}.it.cur .c{color:#3B4A5E}

''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="hd"><b>Destacados</b><span id="hn">Espíritu Imperial</span></div><div class="gr" id="gr"></div>' + BAR + '</div>', r'''
window.onLive=function(d){var a=d.ag||{},L=a.items||[],c=a.cur||0,rev=a.reveal!==false;var n=L.length,cols=n<=4?n||1:n<=8?4:n<=12?4:5,rows=Math.ceil(n/cols)||1;
 var g=document.getElementById('gr');g.style.setProperty('--cols',cols);g.style.setProperty('--h',Math.min(250,Math.floor((600-(rows-1)*20)/rows))+'px');
 document.getElementById('hn').textContent=n?(n+' sucursales'):'';
 var h=L.map(function(it,i){var fut=i>c&&rev;return '<div class="it'+(i===c?' cur':fut?' fut':'')+'" style="animation-delay:'+(i*.04)+'s"><div class="s">'+esc(it.t||'')+'</div><div><div class="n">'+(fut?'Por revelar':esc(it.o||''))+'</div><div class="c">'+(fut?'':esc(it.c||''))+'</div></div></div>'}).join('');
 if(g.dataset.k!==h){g.dataset.k=h;g.innerHTML=h}};''')

# =========================================================== PAUSA
P['IMP_Pausa'] = page('Espíritu Imperial · Pausa', r'''
.c{position:absolute;left:0;right:0;top:270px;text-align:center;display:flex;flex-direction:column;align-items:center}
.t{font-family:"Roboto Condensed";font-weight:900;font-size:150px;line-height:.92;text-transform:uppercase;animation:rise 1s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin:32px auto 0;transform-origin:center}
.s{font-size:40px;margin-top:26px;animation:up .8s .2s ease both}
.clk{font-family:"Roboto Condensed";font-weight:900;font-size:96px;font-variant-numeric:tabular-nums;margin-top:26px;color:var(--wh)}
.next{display:inline-flex;align-items:center;gap:24px;margin-top:30px;background:rgba(3,21,43,.7);border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:12px 40px 12px 14px;animation:up .8s .3s ease both;max-width:1500px}
.next small{background:var(--rd2);font-family:"Roboto Condensed";font-weight:700;font-size:26px;letter-spacing:2px;text-transform:uppercase;padding:10px 24px;border-radius:999px;white-space:nowrap}
.next b{font-family:"Roboto Condensed";font-size:38px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="c"><div class="t" id="pt">Volvemos en unos minutos</div><div class="rule"></div><div class="s" id="ps"></div>'
 + '<div class="clk hide" id="pc">05:00</div><div class="next hide" id="pn"><small>A continuación</small><b id="pnt"></b></div></div>'
 + BAR + '</div>', r'''
var END=null;
window.onLive=function(d){var p=d.pau||{};document.getElementById('pt').textContent=p.titulo||'Volvemos en unos minutos';document.getElementById('ps').textContent=p.sub||'';
 END=p.end||null;var a=d.ag||{},it=(a.items||[])[a.next!=null?a.next:(a.cur||0)+1];
 var n=document.getElementById('pn');n.classList.toggle('hide',!it||!p.next);if(it)document.getElementById('pnt').textContent='Sucursal '+(it.t||'');tick()};
function tick(){var c=document.getElementById('pc');if(!END){c.classList.add('hide');return}c.classList.remove('hide');var r=Math.max(0,Math.round((END-Date.now())/1000));c.textContent=String(Math.floor(r/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0')}
setInterval(tick,250);''')

# =========================================================== FINAL
P['IMP_Final'] = page('Espíritu Imperial · Final', r'''
.c{position:absolute;left:0;right:0;top:260px;text-align:center;display:flex;flex-direction:column;align-items:center}
.k1{font-family:"Roboto Condensed";font-size:52px;letter-spacing:18px;text-transform:uppercase;color:var(--mu);margin-right:-18px;animation:up .9s ease both}
.t{font-family:"Roboto Condensed";font-weight:900;font-size:150px;line-height:.92;text-transform:uppercase;margin-top:20px;max-width:1700px;animation:rise 1.1s .15s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin:32px auto 0;transform-origin:center}
.s{font-size:40px;margin-top:26px;animation:up .9s .4s ease both}
''', '<div class="stage">' + BG + '<img class="logo" src="' + LOGO + '" alt="Imperial">'
 + '<div class="c"><div class="k1">Espíritu Imperial</div><div class="t" id="ft">Gracias por acompañarnos</div><div class="rule"></div><div class="s" id="fs" data-ev="nombre">Nombre del evento</div></div>'
 + BAR + '</div>', r'''
window.onLive=function(d){var f=d.fin||{};document.getElementById('ft').textContent=f.titulo||'Gracias por acompañarnos';if(f.sub)document.getElementById('fs').textContent=f.sub};''')

# =========================================================== LOWER THIRD (overlay)
P['IMP_Overlay_LowerThird'] = page('Espíritu Imperial · Lower third', r'''
#lt{position:absolute;left:96px;bottom:110px;display:flex;align-items:stretch;visibility:hidden;transition:bottom .4s}
#lt.up{bottom:210px}
#lt.in,#lt.out{visibility:visible}
.rd{width:14px;background:var(--rd);border-radius:6px 0 0 6px}
.card{position:relative;background:linear-gradient(100deg,#063661,#0A2F5E 70%,#041F3D);padding:20px 60px 22px 34px;min-width:620px;box-shadow:0 18px 50px rgba(0,0,0,.35);overflow:hidden;border-radius:0 8px 8px 0}
.card::after{content:"";position:absolute;top:0;bottom:0;width:140px;left:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.16),transparent);transform:translateX(-200%) skewX(-18deg)}
.nm{font-family:"Roboto Condensed";font-size:58px;font-weight:900;line-height:1.02;text-transform:uppercase;white-space:nowrap}
.cg{font-size:30px;font-weight:500;margin-top:4px;white-space:nowrap;color:var(--mu)}
.cg b{color:var(--wh);font-weight:500}
.su{position:absolute;left:14px;top:-44px;background:var(--rd2);font-family:"Roboto Condensed";font-weight:700;font-size:24px;letter-spacing:1.5px;text-transform:uppercase;padding:8px 20px;border-radius:6px 6px 0 0;white-space:nowrap}
#lt.in .rd{animation:upy .5s cubic-bezier(.16,1,.3,1) both}
#lt.in .card{animation:wipe .7s .1s cubic-bezier(.7,0,.2,1) both}
#lt.in .card::after{animation:sweep 1.4s .9s ease-in-out both}
#lt.in .nm{animation:left .6s .35s ease both}
#lt.in .cg{animation:left .6s .48s ease both}
#lt.in .su{animation:upy .5s .6s cubic-bezier(.16,1,.3,1) both}
@keyframes upy{from{transform:scaleY(0)}to{transform:none}}
@keyframes wipe{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
#lt.out .nm,#lt.out .cg,#lt.out .su{animation:fadeo .25s ease both}
#lt.out .card{animation:wipeo .45s .15s cubic-bezier(.7,0,.3,1) both}
#lt.out .rd{animation:fadeo .3s .5s ease both}
@keyframes fadeo{to{opacity:0;transform:translateY(-12px)}}
@keyframes wipeo{from{clip-path:inset(0 0 0 0)}to{clip-path:inset(0 100% 0 0)}}
''', '<div id="lt"><div class="su" id="su">Sucursal</div><div class="rd"></div><div class="card"><div class="nm" id="nm" data-max="58" data-min="34" data-fit="w">Nombre Apellido</div><div class="cg" id="cg">Cargo</div></div></div>', r'''
var V=false,K='';
function render(l){document.getElementById('nm').textContent=l.nombre||'Nombre Apellido';document.getElementById('cg').textContent=l.cargo||'';
 var s=document.getElementById('su');s.textContent=l.empresa?('Sucursal '+l.empresa):'';s.classList.toggle('hide',!l.empresa);
 var w=Math.max(document.getElementById('nm').scrollWidth,document.getElementById('cg').scrollWidth);document.querySelector('.card').style.width=Math.min(1500,Math.max(620,w+100))+'px';fitAll()}
function play(c){var el=document.getElementById('lt');el.classList.remove('in','out');void el.offsetWidth;if(c)el.classList.add(c)}
window.onLive=function(d){var show=!!(d.show&&d.show.lt),l=d.lt||{},k=JSON.stringify(l);
 document.getElementById('lt').classList.toggle('up',!!(d.show&&d.show.msg));
 if(show&&(!V||k!==K)){var go=function(){K=k;render(l);play('in')};if(V){play('out');setTimeout(go,850)}else go();V=true}
 else if(!show&&V){V=false;play('out')}};
if(Q.get('demo'))setTimeout(function(){window.onLive({show:{lt:true},lt:{nombre:'Nombre Apellido',cargo:'Vendedor especialista',empresa:'Maipú'}})},300);''', full=False)

# =========================================================== MOSCA (overlay)
P['IMP_Overlay_Mosca'] = page('Espíritu Imperial · Mosca', r'''
.mo{position:absolute;right:60px;top:52px;display:flex;flex-direction:column;align-items:flex-end;gap:10px;transform-origin:right top;transition:opacity .4s,transform .35s}
.mo.bl,.mo.tl{right:auto;left:60px;align-items:flex-start;transform-origin:left top}
.mo.br,.mo.bl{top:auto;bottom:52px;flex-direction:column-reverse;transform-origin:right bottom}
.mo.bl{transform-origin:left bottom}
.mo img{width:240px;filter:drop-shadow(0 3px 10px rgba(0,0,0,.6))}
.mo .row{display:flex;gap:10px;align-items:center}
.live{display:flex;align-items:center;gap:10px;background:var(--rd2);border-radius:6px;padding:6px 16px 6px 12px;font-family:"Roboto Condensed";font-weight:700;font-size:22px;letter-spacing:1.5px;box-shadow:0 6px 18px rgba(0,0,0,.3)}
.live i{width:10px;height:10px;border-radius:50%;background:#fff;animation:pulse 2s ease-in-out infinite}
.msg{background:rgba(4,31,61,.9);border:1px solid rgba(255,255,255,.2);border-radius:6px;padding:6px 16px;font-family:"Roboto Condensed";font-weight:700;font-size:22px;max-width:560px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:opacity .5s}
.msg.off{opacity:0}
''', '<div class="mo" id="mo"><img src="' + LOGO + '" alt="Imperial"><div class="row"><div class="msg" id="msg">#EspírituImperial</div><div class="live" id="live"><i></i><span id="est">EN VIVO</span></div></div></div>', r'''
var MS=[],mi=0,C={pos:'tr',scale:1,op:1,live:true,msgs:true},SH=true;
function apply(){var m=document.getElementById('mo');m.className='mo '+(C.pos||'tr');m.style.transform='scale('+(+C.scale||1)+')';m.style.opacity=SH?(C.op==null?1:C.op):0;
 if(/^b/.test(C.pos)&&C.avoid)m.style.bottom=C.avoid+'px';else m.style.bottom='';
 document.getElementById('live').classList.toggle('hide',!C.live);document.getElementById('msg').classList.toggle('hide',!C.msgs||!MS.length);document.getElementById('est').textContent=C.estado||'EN VIVO'}
window.onLive=function(d){if(d.mosca){C=d.mosca;MS=C.list||[]}SH=!(d.show&&d.show.mosca===false);if(mi>=MS.length)mi=0;document.getElementById('msg').textContent=MS[mi]||'';apply()};
setInterval(function(){if(MS.length<2)return;var el=document.getElementById('msg');el.classList.add('off');setTimeout(function(){mi=(mi+1)%MS.length;el.textContent=MS[mi];el.classList.remove('off')},550)},6000);apply();''', full=False)

# =========================================================== SUCURSAL EN PANTALLA (overlay arriba a la izquierda)
P['IMP_Overlay_Tema'] = page('Espíritu Imperial · Sucursal en pantalla', r'''
#tm{position:absolute;left:60px;top:56px;display:flex;align-items:stretch;max-width:1180px;visibility:hidden}
#tm.in,#tm.out{visibility:visible}
.k{background:var(--rd2);font-family:"Roboto Condensed";font-weight:700;font-size:24px;letter-spacing:1.5px;text-transform:uppercase;padding:0 20px;border-radius:6px 0 0 6px;display:flex;align-items:center}
.t{background:rgba(4,31,61,.92);border:1px solid rgba(255,255,255,.16);border-left:0;font-family:"Roboto Condensed";font-size:32px;font-weight:700;padding:10px 28px 10px 22px;border-radius:0 6px 6px 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;box-shadow:0 10px 30px rgba(0,0,0,.25);text-transform:uppercase}
.t span{font-family:"Roboto";font-weight:400;color:var(--mu);font-size:24px;margin-left:12px;text-transform:none}
#tm.in .k{animation:upy .45s cubic-bezier(.16,1,.3,1) both}
#tm.in .t{animation:wipe .6s .1s cubic-bezier(.7,0,.2,1) both}
#tm.out{animation:fo .4s ease both}
@keyframes upy{from{transform:scaleY(0)}to{transform:none}}
@keyframes wipe{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes fo{to{opacity:0;transform:translateY(-20px)}}
''', '<div id="tm"><div class="k" id="tk">Sucursal</div><div class="t" id="tt">Nombre sucursal</div></div>', r'''
var V=false,K='';
window.onLive=function(d){var s=!!(d.show&&d.show.tema),t=d.tema||{},k=JSON.stringify(t),el=document.getElementById('tm');
 var go=function(){K=k;document.getElementById('tk').textContent=t.kicker||'Sucursal';document.getElementById('tt').innerHTML=esc(t.titulo||'')+(t.sub?'<span>'+esc(t.sub)+'</span>':'');el.classList.remove('in','out');void el.offsetWidth;el.classList.add('in')};
 if(s&&(!V||k!==K)){if(V){el.classList.remove('in');el.classList.add('out');setTimeout(go,420)}else go();V=true}
 else if(!s&&V){V=false;el.classList.remove('in');el.classList.add('out')}};''', full=False)

# =========================================================== MENSAJE (zócalo inferior)
P['IMP_Overlay_Mensaje'] = page('Espíritu Imperial · Mensaje', r'''
#zc{position:absolute;left:0;right:0;bottom:0;height:84px;display:flex;align-items:stretch;transform:translateY(110%);transition:transform .6s cubic-bezier(.7,0,.2,1);border-top:4px solid var(--rd)}
#zc.on{transform:none}
.lb{flex:none;background:var(--rd2);font-family:"Roboto Condensed";font-weight:900;font-size:30px;letter-spacing:1.5px;text-transform:uppercase;display:flex;align-items:center;gap:18px;padding:0 36px 0 50px}
.lb img{height:38px}
.tx{flex:1;background:rgba(4,31,61,.96);padding-left:36px;display:flex;align-items:center;overflow:hidden;position:relative}
.tx span{font-size:34px;font-weight:500;white-space:nowrap}
.tx.mv span{animation:tick var(--d,20s) linear infinite;padding-left:100%}
@keyframes tick{from{transform:translateX(0)}to{transform:translateX(-100%)}}
''', '<div id="zc"><div class="lb"><span id="zl">Saludos</span></div><div class="tx" id="ztx"><span id="zt">Mensaje</span></div></div>', r'''
var K='',IT=[],ii=0,TT=null;
function showItem(){var sp=document.getElementById('zt'),box=document.getElementById('ztx');sp.textContent=IT[ii]||'';box.classList.remove('mv');
 requestAnimationFrame(function(){if(sp.scrollWidth>box.clientWidth-80){box.style.setProperty('--d',Math.max(10,sp.scrollWidth/140)+'s');box.classList.add('mv')}})}
window.onLive=function(d){var on=!!(d.show&&d.show.msg),m=d.msg||{};document.getElementById('zc').classList.toggle('on',on);
 var k=JSON.stringify(m);if(k===K)return;K=k;document.getElementById('zl').textContent=m.label||'Saludos';IT=(m.items||[]).filter(Boolean);ii=0;showItem();
 clearInterval(TT);if(IT.length>1)TT=setInterval(function(){ii=(ii+1)%IT.length;showItem()},(+m.every||10)*1000)};''', full=False)

# =========================================================== REPETICIÓN (overlay)
P['IMP_Overlay_Replay'] = page('Espíritu Imperial · Repetición', r'''
.rp{position:absolute;left:60px;top:52px;display:flex;align-items:center;gap:14px;background:var(--rd2);border-radius:8px;padding:10px 28px 10px 12px;box-shadow:0 10px 30px rgba(0,0,0,.35);animation:left .5s cubic-bezier(.16,1,.3,1) both}
.rp .ic{width:52px;height:52px;border-radius:6px;background:var(--dk);display:flex;align-items:center;justify-content:center}
.rp .ic svg{width:30px;height:30px;fill:#fff}
.rp b{font-family:"Roboto Condensed";font-size:34px;font-weight:900;letter-spacing:2px;text-transform:uppercase}
.rec{position:absolute;inset:0;border:8px solid rgba(200,16,46,.6);pointer-events:none}
''', '<div class="rec"></div><div class="rp"><div class="ic"><svg viewBox="0 0 24 24"><path d="M11 6v12L2 12zM21 6v12l-9-6z"/></svg></div><b id="rt">Repetición</b></div>', r'''
window.onLive=function(d){if(d.replay&&d.replay.texto)document.getElementById('rt').textContent=d.replay.texto};''', full=False)


# =========================================================== PICTURE IN PICTURE (marcos con ventanas transparentes)
import sys; sys.path.insert(0, '/home/claude')
import pipgen
PIPCSS = r"""
body{background:transparent!important}
.pbg{position:absolute;inset:0;overflow:hidden;background:radial-gradient(1300px 760px at 50% -14%,rgba(92,146,214,.42),transparent 62%),radial-gradient(1100px 420px at 50% 112%,rgba(237,41,57,.20),transparent 70%),linear-gradient(180deg,#0A2F5E 0%,#063661 38%,#041F3D 100%)}
.pbg .floor{bottom:60px}
.win{position:absolute;border-radius:10px;box-shadow:0 0 0 3px rgba(255,255,255,.9),0 0 0 9px rgba(237,41,57,.0),0 26px 60px rgba(0,0,0,.5)}
.plogo{position:absolute;top:56px;right:70px;width:240px}
.ptitle{position:absolute;left:60px;top:64px;max-width:1300px;font-family:"Roboto Condensed";font-size:64px;font-weight:900;text-transform:uppercase;line-height:1.05;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lab{position:absolute;display:inline-flex;align-items:baseline;gap:14px;background:rgba(3,21,43,.94);border-top:4px solid var(--rd);border-radius:0 0 8px 8px;padding:8px 24px 12px;box-shadow:0 12px 30px rgba(0,0,0,.35);white-space:nowrap;overflow:hidden}
.lab b{font-family:"Roboto Condensed";font-size:32px;font-weight:900;text-transform:uppercase;overflow:hidden;text-overflow:ellipsis}
.lab span{font-size:22px;color:var(--mu)}
"""
for k, L in pipgen.LAYOUTS.items():
    P['IMP_PIP_' + k] = page('Espíritu Imperial · PiP ' + L['nombre'], PIPCSS, pipgen.body(k, BG, LOGO), pipgen.js(k, 10))

os.makedirs('out', exist_ok=True)
for k, v in P.items():
    open('out/%s.html' % k, 'w').write(v)
print(list(P))
