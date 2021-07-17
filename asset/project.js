$(document).ready(function(){
  $('#cid').append($('<option>').text('-Select Category-'))
  $('#btn').click(function () {
    // $('#stext').keyup(function () {
      

       $.getJSON('http://127.0.0.1:8000/searchpagejson/',{ajax:true,pat:$('#stext').val()},function(data){
           htm=''
          // alert(data.length)
           if(data.length==0)
           {htm+="<h1>Record Not Found...</h1>"}
           else {
               htm += "<div class='row'>"


               $.each(data, function (index, item) {

                   htm += "<div class='col-md-4'>"
                   htm += "<div class='category-item'>"
                   htm += "<img src='/static/" + item[10] + "'>"
                   htm += "<div class='ci-text'>"
                   htm += "<h4>" + item[2] + "</h4>"
                   htm += "<p>" + item[7] + "</p>"
                   htm += "</div>"
                   htm += "<a href='/playsong?sg=" + item + "' class='ci-link'><i class='fa fa-play'></i></a>"
                   htm += "</div>"
                   htm += "</div>"


               })
               htm += "</div>"
           }
   $('#result').html(htm)
  })
  })
  $.getJSON('http://127.0.0.1:8000/categorydisplayalljson/',function(data){
   // alert(data)
   $.each(data,function(index,item){
      $('#cid').append($('<option>').text(item[1]).val(item[0]))

   })
  })
    $('#cid').change(function () {


         $.getJSON('http://127.0.0.1:8000/displaysubcategoryjson/',{ajax:true,cid:$('#cid').val()},function(data){

             $('#scid').empty()
              $('#scid').append($('<option>').text('-Select SubCategory-'))
            $.each(data,function(index,item){


             $('#scid').append($('<option>').text(item[2]).val(item[0]))

   })
  })
    })


})