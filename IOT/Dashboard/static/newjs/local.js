function auth(){
      var idu = document.getElementById('user_id').value;
      var psu = document.getElementById('pass').value;
      prompt('Welcome');

        {%for i in room1%}

            if ({{i.id_room1}} == idu){

               if ({{i.room_pass}} == psu){
                     window.open("/ind");
                     var a = true;
               }
               else{
                     var a = false;

               }
            }
            else {
            var a = false;
            }
        {%endfor%}
         if (a==false){
             prompt('User Id or Password are False');
         }
      }