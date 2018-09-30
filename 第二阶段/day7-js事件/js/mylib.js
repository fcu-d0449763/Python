function bind(elem,en,fn){
	if(elem.addEventListener){
		elem.addEventListener(en,fn);
	}else{
		elem.attachEvent("on"+en,fn);
	}
	
}
function unbind(elem,en,fn){
	if(elem.removeEventListener){
		elem.removeEventListener(en,fn);
	}else{
		elem.detachEvent('on'+en,fn);
	}
	
}
