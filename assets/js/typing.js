document.addEventListener('DOMContentLoaded', function() {
    const codeElement = document.getElementById('typed-code');
    if (!codeElement) return;

    const codeText = `let owlhub = {
    mission: "Transformer vos données en décisions",
    expertise: ["Power BI", "DAX", "Power Query"],
    clients_satisfaits: 47,
    projets_livres: 89,

    illuminate: function() {
        return "🦉 Voir clair dans vos données";
    }
};

console.log(owlhub.illuminate());`;

    let index = 0;
    const speed = 30;

    function typeCode() {
        if (index < codeText.length) {
            codeElement.textContent += codeText.charAt(index);
            index++;
            setTimeout(typeCode, speed);
        }
    }

    setTimeout(typeCode, 500);
});
