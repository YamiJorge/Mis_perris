function validarFechaMenorActual(date){
      var x=new Date();
      var fecha = date.split("/");
      x.setFullYear(fecha[2],fecha[1]-1,fecha[0]);
      var today = new Date();
 
      if (x >= today)
        return false;
      else
        return true;
}


if(validarFechaMenorActual(date)){
        alert("La fecha introducida es correcta.");
      
}else{
      alert("El formato de la fecha es incorrecto.");
}