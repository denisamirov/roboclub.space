    window.onload = function () {
  
        var seconds = 00; 
        var tens = 00; 
        var appendTens = document.getElementById("tens")
        var appendSeconds = document.getElementById("seconds")
        var buttonStart = document.getElementById('button-start');
        var buttonStop = document.getElementById('button-stop');
        var buttonReset = document.getElementById('button-reset');
        var buttonText = document.getElementById('b-text');

        var p_first = document.getElementById('1_class');
        var p_sec = document.getElementById('2_class');
        var p_th = document.getElementById('3_class');
        var p_fo = document.getElementById('4_class');
        var p_adult = document.getElementById('adult');
        var p_back = document.getElementById('back');

        var p_first_cl_text = document.getElementById('first_text');
        var p_second_cl_text = document.getElementById('second_text');
        var p_three_cl_text = document.getElementById('three_text');
        var p_four_cl_text = document.getElementById('four_text');
        var p_adults_cl_text = document.getElementById('adults_text');

        var text = document.getElementById('text');
        var menu = document.getElementById('menu');

        var s_plus = document.getElementById('size_plus');
        var s_minus = document.getElementById('size_minus');
        var f_plus = document.getElementById('field_plus');
        var f_minus = document.getElementById('field_minus');
        var instrument = document.getElementById('instruments');
        
        

        var Interval;

        f_minus.onclick = function() {
          x = text.rows;
          text.rows = x - 5;
                  } 


        s_plus.onclick = function() {
          console.log(text.fontSize)
          text.style.fontSize ='210' + '%';
                  }

        s_minus.onclick = function() {
          text.style.fontSize ='95%';
                  }

        f_plus.onclick = function() {
          x = text.rows;
          text.rows = x + 5;
                  }         
          
                 
        buttonStart.onclick = function() {
          
           clearInterval(Interval);
           Interval = setInterval(startTimer, 1000);
           document.getElementById('result').style.opacity = '0%';
           buttonStart.style.display = 'none';
           buttonReset.style.display = 'none';
           buttonText.style.display = 'none';
           s_plus.style.display = 'none';
           f_plus.style.display = 'none';
           s_minus.style.display = 'none';
           f_minus.style.display = 'none'; }

        p_first.onclick = function() {
           p_first.style.display = 'none';
           p_sec.style.display = 'none';
           p_th.style.display = 'none';
           p_fo.style.display = 'none';
           p_adult.style.display = 'none';
           p_first_cl_text.style.display = 'block'
            // Запрос на json получение списка из книг, которые есть в базе
            
        }

        buttonText.onclick = function() {
          menu.classList.toggle('open-nav');
          text.value = 'Выберите текст';
          text.rows = 2;
          console.log(text.rows);
          
           
       }

        p_sec.onclick = function() {
          p_first.style.display = 'none';
          p_sec.style.display = 'none';
          p_th.style.display = 'none';
          p_fo.style.display = 'none';
          p_adult.style.display = 'none';
          p_second_cl_text.style.display = 'block'
           // Запрос на json получение списка из книг, которые есть в базе
           
       }


       p_th.onclick = function() {
        p_first.style.display = 'none';
        p_sec.style.display = 'none';
        p_th.style.display = 'none';
        p_fo.style.display = 'none';
        p_adult.style.display = 'none';
        p_three_cl_text.style.display = 'block'
         // Запрос на json получение списка из книг, которые есть в базе
         
     }


     p_fo.onclick = function() {
      p_first.style.display = 'none';
      p_sec.style.display = 'none';
      p_th.style.display = 'none';
      p_fo.style.display = 'none';
      p_adult.style.display = 'none';
      p_four_cl_text.style.display = 'block'
       // Запрос на json получение списка из книг, которые есть в базе
       
   }

   p_adult.onclick = function() {
    p_first.style.display = 'none';
    p_sec.style.display = 'none';
    p_th.style.display = 'none';
    p_fo.style.display = 'none';
    p_adult.style.display = 'none';
    p_adults_cl_text.style.display = 'block'

          
 }

 jQuery(function($) {
  $('.lot_of_texts').click(function() {
    const el = $(this);
    console.log(el.text(), el.data("lot_of_texts"))
    var a = el.text();
    // console.log(a)
    menu.classList.replace('open-nav', 'full-screen-nav');


    $.ajax(
      {
      url: `http://127.0.0.1:8000/text/${a}/`,
      dataType: 'json',
      success: function(data) {
      console.log(data.x[0].text);

      let count = 1;
      split = data.x[0].text
      console.log('text', split)

      for (var i = 0; i < split.length ; i++)
       {
        if (split[i] == " ") 
          {
            count += 1;
          }
        }

      document.getElementById("number_of_wordse").innerHTML = count;                       
      document.getElementById("text").value = data.x[0].text;
      $("#text").val(data.x[0].text);
      text.rows = 10;
    }


    });

  });
});


        p_back.onclick = function() {
          p_first.style.display = 'block';
          p_sec.style.display = 'block';
          p_th.style.display = 'block';
          p_fo.style.display = 'block';
          p_adult.style.display = 'block';
          p_first_cl_text.style.display = 'none'
          p_second_cl_text.style.display = 'none'
          p_three_cl_text.style.display = 'none'
          p_four_cl_text.style.display = 'none'
          p_adults_cl_text.style.display = 'none'
       }
        
          buttonStop.onclick = function() {
             clearInterval(Interval);
             text.rows = 2;
             var Row = document.getElementById("q");
             var Cells = Row.getElementsByTagName("td");
             var count = Cells[1].innerText;
                console.log('Количество слов', count);
                o = seconds*60 + tens;
                console.log('Время', o);

             document.getElementById("speed").innerHTML = Math.round((count*60 / o));
             
             document.getElementById("timee").innerHTML = o;
             document.getElementById('result').style.opacity = '100%';
             buttonStart.style.display = 'inline-block';
             buttonReset.style.display = 'inline-block';
             buttonText.style.display = 'inline-block';
             s_plus.style.display = 'inline-block';
             f_plus.style.display = 'inline-block';
             s_minus.style.display = 'inline-block';
             f_minus.style.display = 'inline-block';

    
        }
        
      
        buttonReset.onclick = function() {
           clearInterval(Interval);
          tens = "00";
            seconds = "00";
          appendTens.innerHTML = tens;
            appendSeconds.innerHTML = seconds;
        }
        
         
        
        function startTimer () {
          tens++; 
          
          if(tens <= 9){
            appendTens.innerHTML = "0" + tens;
          }
          
          if (tens > 9){
            appendTens.innerHTML = tens;
            
          } 
          
          if (tens > 99) {
            console.log("seconds");
            seconds++;
            appendSeconds.innerHTML = "0" + seconds;
            tens = 0;
            appendTens.innerHTML = "0" + 0;
          }
          
          if (seconds > 9){
            appendSeconds.innerHTML = seconds;
          }
        
        }
        
        const trigger = document.querySelector('.trigger');
        const nav = document.querySelector('.full-screen-nav');
        const backdrop = document.querySelector('.backdrop');
        
        trigger.addEventListener('click', () => nav.classList.add('open-nav'));
        backdrop.addEventListener('click', () => nav.classList.remove('open-nav'));
        
      }





