// personaje de tv
let name = "jordan";
let tv = "tc";
let edad = 19;
let personaje ={
    name: "jordan",
    tv : "tc",
    edad: 19,
}; 
console.log( personaje)
console.log( personaje.edad)
console.log( personaje['name'])
personaje.edad=17;
personaje['edad']= 16;
delete personaje.name;
console.log(personaje)