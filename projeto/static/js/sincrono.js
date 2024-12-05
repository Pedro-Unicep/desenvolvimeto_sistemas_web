console.log('1');
console.log('2');
// Simulação de leitura síncrona usando XMLHttpRequest
var request = new XMLHttpRequest();
request.open('GET', '/fetch-teste-txt/', false); // false para síncrono
request.send(null);
if (request.status === 200) { // O código 200 significa que a requisição foi perfeita!
console.log(request.responseText);
}
console.log('3');
