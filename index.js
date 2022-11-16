const ledOn = document.getElementById('ledEncender');
const ledOff = document.getElementById('ledApagar');

ledOn.addEventListener(('click'),()=>{
    const options = {method: 'GET'};
    fetch('http://172.20.10.9:5000/led/encender', options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));
})

ledOff.addEventListener(('click'),()=>{
    const options = {method: 'GET'};
    fetch('http://172.20.10.9:5000/led/apagar', options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));
})