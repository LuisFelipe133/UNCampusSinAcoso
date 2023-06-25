const btnAbrirDescripcion =
document.querySelector("#btn-abrir-denuncia");

const btnCerrarDescipcion =
document.querySelector("#btn-cerrar-denuncia");

const modal =
document.querySelector("#denuncia");
    
btnAbrirDescripcion.addEventListener("click",()=>{
    modal.showModal(); 
})

btnCerrarDescipcion.addEventListener("click",()=>{
    modal.close();
})