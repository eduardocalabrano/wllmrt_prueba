$(".btn_verProd").click(function() {
  alert('Detalle Producto')
});

$('#btn_buscaProducto').click(function(){
  $("#section_listaProductos").addClass("oculto");
  $("#section_mensajeBuscando").removeClass("oculto");
  let prod_buscar = $("#inpt_busqueda").val();
  let descuento_50 = false;
  // $("#btn_buscaProducto").attr("href", "/filtro/marca");
  if(prod_buscar.length >= 3){
    $.ajax({
      url: '/ajax/valida_palidromo/',
      data: {
        'prod_buscar': prod_buscar
      },
      dataType: 'text'
    }).done(function( data ){
      if(data == 'Y'){
        descuento_50 = true;
      }
      window.location.replace("/filtro/"+prod_buscar);
      // realizar_busqueda(descuento_50, prod_buscar)
    }).fail(function(){
      alert( "Algo salió mal. Intente nuevamente");
    });
  }
  else{
    window.location.replace("/filtro/"+prod_buscar);
  }
  //Fin llamada AJAX
});
