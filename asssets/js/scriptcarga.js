

document.getElementById('form-personaje').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const nombre = document.getElementById('nombre').value;
    const clase = document.getElementById('clase').value;
    
    document.getElementById('nombre-personaje').textContent = nombre;
    document.getElementById('clase-personaje').textContent = clase;
    document.getElementById('creacion-personaje').style.display = 'none';
    document.getElementById('interfaz-juego').style.display = 'block';
});

document.getElementById('atacar').addEventListener('click', function() {
    const daño = Math.floor(Math.random() * 10) + 1;
    document.getElementById('daño').textContent = `Hiciste ${daño} puntos de daño!`;
});

document.getElementById('sanar').addEventListener('click', function() {
    document.getElementById('daño').textContent = `Te has sanado!`;
});
