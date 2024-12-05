console.log('1');
console.log('2');
// Fetch API assíncrona
fetch('/fetch-teste-txt/')
.then(response => response.text())
.then(data => console.log(data))
.catch(error => console.error('Erro:', error));
console.log('3')