var CC_STORE = function () {
    var customers = {};
    var products = {};

    function Customer(name) {
        var cart = [];

        function CartItem(qty, product) {
        }

        return {
            name: name,
            cart: cart
        }
    }

    function Product(name, price) {
        this.name = name;
        this.price = price;
        return {
            name: this.name,
            price: this.price
        }
    }


    function addCustomer(name) {
        customers[name] = new Customer(name);
    }

    function addProduct(name, price) {
        products[name] = new Product(name, price);
    }

    return {
        customer_list: customer_list
    }
}();

CC_STORE.addCustomer("Kevin");
