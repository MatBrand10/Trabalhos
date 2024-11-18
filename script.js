// script.js

// Função para captura de dados do usuário na index.html
document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o envio do formulário
    const name = document.getElementById("name").value;
    const age = parseInt(document.getElementById("age").value);
    document.getElementById("result").innerText = Nome;{name}Idade;{age};
});

// Função para calcular a soma na index.html
document.getElementById("calculationForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o envio do formulário
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const sum = num1 + num2;
    document.getElementById("calculationResult").innerText = soma;{sum};
});