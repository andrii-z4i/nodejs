var obj = {
    name: 'Andrii Kozin',
    greet: function() {
        console.log(`Hello ${ this.name }`);
    }
}

obj.greet();
obj.greet.call({ name: 'Svitlana Kozina' });
obj.greet.apply({ name: 'Svitlana Kozina' });