const form = document.getElementById('myForm'); //document es el html
if(form){
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        validateForm();
    });
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,7}$/ //Expresion regular para validar los caracteres del email
        return regex.test(email) //test() es el método para buscar la expresión regular en el string. Devuelve true o false.
    }
    function validateForm() {
        const emailInput = document.getElementById('email');
        const email = emailInput.value;
        if (!validateEmail(email)) {
            alert('Por favor ingrese un correo electrónico válido.');
        } else {
            alert('Consulta enviada correctamente. Pronto nos comunicaremos!.');
        }
    }
}

// function currentTime() {
//     let date = new Date();
//     let hh = date.getHours();
//     let mm = date.getMinutes();
//     let ss = date.getSeconds();

//     hh = (hh < 10) ? "0" + hh : hh;
//     mm = (mm < 10) ? "0" + mm : mm;
//     ss = (ss < 10) ? "0" + ss : ss;

//     let time = hh + ":" + mm + ":" + ss;
//     let watch = document.querySelector('#watch');
//     watch.innerHTML = time;
// } // hasta el reloj que marca la hora actual

// setInterval(currentTime, 1000);

// const getRemainTime = deadline => {
//     let now = new Date(),
//         RemainTime = (new Date(deadline) -)

// }// este seria el reloj  de cuenta regresesiva todabia esta en construccion


//Consumo API conversor de monedas
const monedaEl_one = document.getElementById('moneda-uno');
const monedaEl_two = document.getElementById('moneda-dos');
const cantidadEl_one = document.getElementById('cantidad-uno');
const cantidadEl_two = document.getElementById('cantidad-dos');
const cambioEl = document.getElementById('cambio');
const tasaEl = document.getElementById('tasa');


// Fetch Exchange Rate and Update the DOM
function calculate(){
    const moneda_one = monedaEl_one.value;
    const moneda_two = monedaEl_two.value;
    
   fetch(`https://v6.exchangerate-api.com/v6/90fcb603c8ce2d4ba4d42a03/latest/${moneda_one}`)
   .then(res => res.json() )
   .then(data => {
       const tasa = data.conversion_rates[moneda_two];
       
       cambioEl.innerText = `1 ${moneda_one} = ${tasa} ${moneda_two}`;

       cantidadEl_two.value = (cantidadEl_one.value * tasa).toFixed(2);

    } );
    
}

//Event listeners
monedaEl_one.addEventListener('change', calculate);
cantidadEl_one.addEventListener('input', calculate);
monedaEl_two.addEventListener('change', calculate);
cantidadEl_two.addEventListener('input', calculate);

tasa.addEventListener('click', () =>{
    const temp = monedaEl_one.value;
    monedaEl_one.value = monedaEl_two.value;
    monedaEl_two.value = temp;
    calculate();
} );


calculate();

//Formulario emergente
function reservarDestino() {
    var x=document.getElementById("espacioReserva")
    x.innerHTML=
    `<div id="reserva">
        <form id="registro" action="">
            <legend>Datos personales</legend>
            <br>
            <label for="firstname">Nombres:
            <input type="text" size="24" name="firstname" placeholder="Ingrese su nombre aquí..." required>
            </label>
            <label for="lastname">&nbsp;&nbsp;&nbsp;Apellido:
                <input type="text" size="20" name="lastname" placeholder="Ingrese su apellido aquí..." required>
            </label>                                           
            <label for="city">Destino:
                <input type="text" size="32" name="city" placeholder="Ingrese la ciudad de destino">
            </label>
            <label for="night">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Noches:
                <input type="number" size="10" name="host">
            </label>
            <label for="email">Correo electrónico:
                <input type="email" name="email" size="24" placeholder="Ingrese su correo electrónico" required>
            </label>
            <label for="phone">&nbsp;&nbsp;&nbsp;Teléfono:
                <input type="tel" size="15" name="phone" maxlength="13" placeholder="Ingrese su teléfono">
            </label>
            <label for="date">Fecha de viaje:
                <input type="date" name="fly">
            </label>    
            <label for="gender">&nbsp;&nbsp;&nbsp;Género:
                <input type="radio" name="gender" value="hombre" checked="">Hombre
                <input type="radio" name="gender" value="mujer">Mujer
            </label>
            <label for="price">Precio total:
                <input type="number" value="=esp.value">
            </label>                      
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="CONFIRMAR RESERVA">
        </form>
    </div>`
    window.location.href="#espacioReserva";
}