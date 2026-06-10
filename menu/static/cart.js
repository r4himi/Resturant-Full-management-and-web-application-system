let cart = JSON.parse(localStorage.getItem("cart")) || [];
document.addEventListener("click", function (e) {

    if (e.target.classList.contains("increase")) {

        const id = e.target.dataset.id;

        let item = cart.find(i => i.id == id);

        if (item) {
            item.quantity++;
        } else {

                const menuItem = e.target.closest(".menu-item");

                cart.push({
                    id: id,
                    name: menuItem.dataset.name,
                    price: parseFloat(menuItem.dataset.price),
                    quantity: 1
                });
        }

        saveCart();
        updateCartCount();
        updateItemQty(id);
    }

    if (e.target.classList.contains("decrease")) {

        const id = e.target.dataset.id;

        decreaseQty(id);

        saveCart();
        updateCartCount();
        updateItemQty(id);
    }
});

function decreaseQty(id) {
    const item = cart.find(i => i.id == id);
    if (item) {
        item.quantity--;
        if (item.quantity <= 0) {
            cart = cart.filter(i => i.id != id);
        }
    }
}

function updateItemQty(id) {

    const menuItem = document.querySelector(`.menu-item[data-id="${id}"]`);
    if (!menuItem) return;

    const item = cart.find(i => i.id == id);
    const qtySpan = menuItem.querySelector(".qty");

    if (qtySpan) {
        qtySpan.innerText = item ? item.quantity : 0;
    }
}

/* SAVE */
function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

/* UPDATE CART COUNT */
function updateCartCount() {
  const cartCount = document.getElementById("cartCount");
  if (!cartCount) return;

  let total = 0;
  cart.forEach(item => total += item.quantity);

  cartCount.innerText = total;
}

/* ADD TO CART */
function addToCart(id, name, price) {

    let item = cart.find(i => i.id == id);

    if (item) {
        item.quantity++;
    } else {
        cart.push({
            id: id,
            name: name,
            price: parseFloat(price),
            quantity: 1
        });
    }

    saveCart();
    updateCartCount();

    updateItemQty(id); // 🔥 THIS FIXES YOUR ISSUE
}

/* INIT */
document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".add-to-cart").forEach(button => {

        button.addEventListener("click", function () {

            addToCart(
                this.dataset.id,
                this.dataset.name,
                this.dataset.price
            );
        });

    });

    // restore quantities on reload
    cart.forEach(item => {
        updateItemQty(item.id);
    });

    updateCartCount();
});