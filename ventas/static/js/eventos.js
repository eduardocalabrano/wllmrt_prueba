$(".btn_verProd").click(function() {
  alert('Detalle Producto')
});

$('#btn_buscaProducto').click(function(){
  let prod_buscar = $("#inpt_busqueda").val();
  if(parseInt(prod_buscar) || prod_buscar.length >= 3){
    $("#section_listaProductos").addClass("oculto");
    $("#section_mensajeBuscando").removeClass("oculto");
    window.location.replace("/filtro/"+prod_buscar);
  }
  else{
    // Insertar algún mensaje al usuario
  }
});
