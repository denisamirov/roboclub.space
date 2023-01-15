function init() {

    document.querySelector("#button_check").onclick = function() {
        a = Number(first_1('number_of_servo', 'servo_power'));
        b = Number(first_1('number_of_logic', 'logic_power'));
        c = Number(first_1('number_of_hold', 'hold_power'));
        d = Number(first_1('number_of_water', 'water_power'));

        var power_moduls = Number(document.getElementById("power_moduls").value);
        var number_moduls = document.getElementById("number_moduls").value;
        var size_moduls = Number(document.getElementById("size_moduls").value);
        var number_moduls_in_line = Number(document.getElementById("number_moduls_in_line").value);
        var work_in_day = (number_moduls * size_moduls)/ (50*60);
        $('#work_in_day').val(work_in_day);
        $('#consumption_in_day').val((work_in_day*(a+b+c+d)/1000) + (0.05*(work_in_day*(a+b+c+d)/1000)));
        $('#consumption_in_year').val(365*((work_in_day*(a+b+c+d)/1000) + (0.05*(work_in_day*(a+b+c+d)/1000))));

        var power_ss = number_moduls*power_moduls*0.7
        var power_365 = power_ss*365/1000
        var eff = 100 - (((365*((work_in_day*(a+b+c+d)/1000) + (0.05*(work_in_day*(a+b+c+d)/1000))))/power_365)*100)
        $('#eff').val(eff);
    }
    
    function first_1(number, power) {
        var number_of_servo = document.getElementById(number).innerHTML;
        var servo_power = document.getElementById(power).innerHTML;
        return number_of_servo*servo_power
    }


    var toastTrigger = document.getElementById('button_check')
var toastLiveExample = document.getElementById('liveToast')
if (toastTrigger) {
  toastTrigger.addEventListener('click', function () {
    var toast = new bootstrap.Toast(toastLiveExample)

    toast.show()
  })
}

    }
    
    window.onload = init;