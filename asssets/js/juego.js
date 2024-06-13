function characterAttack(character, damage) {
    var monsterHealth = parseInt(document.getElementById('monster-health').textContent);
    var characterHealth = parseInt(document.getElementById(character.toLowerCase() + '-health').textContent);

    // Validar si el personaje está muerto
    if (characterHealth <= 0) {
        alert(character + ' ya está muerto y no puede recibir más daño.');
        return;
    }

    // Aplicar habilidad especial del Caballero
    if (character === 'Caballero') {
        damage *= 0.8; // El Caballero recibe un 20% menos de daño
    }

    var newMonsterHealth = monsterHealth - damage;
    if (newMonsterHealth <= 0) {
        newMonsterHealth = 0;
        alert('¡Has derrotado al monstruo!');
        location.reload(); // Reiniciar la página
    } else {
        document.getElementById('monster-health').textContent = newMonsterHealth;
        
        // Obtener todos los personajes vivos
        var characters = document.querySelectorAll('.character');
        var aliveCharacters = [];
        for (var i = 0; i < characters.length; i++) {
            var targetHealth = parseInt(characters[i].querySelector('h3 span').textContent);
            if (targetHealth > 0) {
                aliveCharacters.push(characters[i]);
            }
        }

        // Si no hay personajes vivos, no hacer nada
        if (aliveCharacters.length === 0) {
            alert('Todos los personajes han sido derrotados.');
            return;
        }

        // Elegir un objetivo al azar de los personajes vivos
        var targetIndex = Math.floor(Math.random() * aliveCharacters.length);
        var target = aliveCharacters[targetIndex];
        var targetName = target.querySelector('h3').textContent.split(':')[0].trim();
        var targetHealth = parseInt(target.querySelector('h3 span').textContent);

        var newTargetHealth = targetHealth - damage;
        target.querySelector('h3 span').textContent = newTargetHealth;
        if (newTargetHealth <= 0) {
            alert('¡' + targetName + ' ha sido derrotado!');
            target.querySelector('img').src = 'asssets/creacion de personajes/muerto.jpeg'; // Ruta de la imagen del cadáver
        }
    }
}
