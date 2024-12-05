const autoNumeric = new AutoNumeric('#id_cost',
    {
        digitGroupSeparator: '.',
        decimalCharacter: ',',
        decimalPlaces: 2,
        currencySymbol: 'R$ ',
        currencySymbolPlacement: 'p',
    })

const form = document.querySelector('form');

form.addEventListener('submit', function(event)
{
    document.getElementById('id_cost').value = autoNumeric.getNumber();
})