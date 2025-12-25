// typing.js - Animation de frappe du code M
document.addEventListener('DOMContentLoaded', function() {
    console.log('⌨️ Typing.js chargé');

    const codeElement = document.getElementById('typed-code');

    if (!codeElement) {
        console.error('❌ #typed-code introuvable');
        return;
    }

    const codeSnippet = `let
    Source = Excel.CurrentWorkbook(){[Name="Data"]}[Content],
    FilteredRows = Table.SelectRows(Source, each [Sales] > 1000),
    AddedColumn = Table.AddColumn(FilteredRows, "Margin", each [Revenue] - [Cost])
in
    AddedColumn`;

    let index = 0;
    let isDeleting = false;

    function typeWriter() {
        if (!isDeleting) {
            // MODE ÉCRITURE
            if (index < codeSnippet.length) {
                codeElement.textContent += codeSnippet.charAt(index);
                index++;
                setTimeout(typeWriter, 30); // Vitesse d'écriture
            } else {
                // Pause avant effacement
                setTimeout(() => {
                    isDeleting = true;
                    typeWriter();
                }, 3000); // Pause 3 secondes
            }
        } else {
            // MODE EFFACEMENT
            if (index > 0) {
                codeElement.textContent = codeSnippet.substring(0, index - 1);
                index--;
                setTimeout(typeWriter, 15); // Vitesse d'effacement (plus rapide)
            } else {
                // Recommencer
                isDeleting = false;
                setTimeout(typeWriter, 500); // Pause 0.5s avant réécriture
            }
        }
    }

    typeWriter();
    console.log('✅ Animation du code démarrée');
});
