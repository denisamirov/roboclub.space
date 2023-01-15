window.onload = function () {
  var first = document.getElementById('first_class');
  var sec = document.getElementById('second_class');
  var th = document.getElementById('third_class');
  var six = document.getElementById('six_class');
  var other = document.getElementById('other_class');

  var buttonFirst = document.getElementById('f');
  var buttonSecond = document.getElementById('s');
  var buttonFour= document.getElementById('fo');
  var buttonSix = document.getElementById('si');
  var buttonOther = document.getElementById('o');
       


buttonFirst.onclick = function() {
     first.style.display = 'inline';
     sec.style.display = 'none';
     th.style.display = 'none';
     six.style.display = 'none';
     other.style.display = 'none';}

buttonSecond.onclick = function() {
     first.style.display = 'none';
     sec.style.display = 'inline';
     th.style.display = 'none';
     six.style.display = 'none';
     other.style.display = 'none';}

buttonFour.onclick = function() {
     first.style.display = 'none';
     sec.style.display = 'none';
     th.style.display = 'inline';
     six.style.display = 'none';
     other.style.display = 'none';}

buttonSix.onclick = function() {
     first.style.display = 'none';
     sec.style.display = 'none';
     th.style.display = 'none';
     six.style.display = 'inline';
     other.style.display = 'none';}

buttonOther.onclick = function() {
     first.style.display = 'none';
     sec.style.display = 'none';
     th.style.display = 'none';
     six.style.display = 'none';
     other.style.display = 'inline';}

 }