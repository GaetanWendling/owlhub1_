// typing.js - Animation de code M avec fenêtre fixe
document.addEventListener('DOMContentLoaded', function() {
    const codeElement = document.getElementById('typed-code');
    if (!codeElement) return;

    const code = `let
    Source = Excel.CurrentWorkbook(){[Name="Data"]}[Content],
    TypeChange = Table.TransformColumnTypes(Source,{
        {"Date", type date},
        {"Montant", type number}
    }),
    AddYear = Table.AddColumn(TypeChange, "Annee",
        each Date.Year([Date]), Int64.Type),
    FilterRows = Table.SelectRows(AddYear,
        each [Montant] > 1000)
in
    FilterRows`;

    let index = 0;
    const speed = 50;

    function typeCode() {
        if (index < code.length) {
            codeElement.textContent += code.charAt(index);
            index++;
            setTimeout(typeCode, speed);
        }
    }

    // Démarrer l'animation après 500ms
    setTimeout(typeCode, 500);
});
