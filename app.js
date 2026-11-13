// Initialize default admin user and sample items in localStorage
function initStorage() {
    if (!localStorage.getItem("users")) {
        const defaultUsers = [
            { fullname: "Admin User", email: "admin@test.com", password: "admin123" }
        ];
        localStorage.setItem("users", JSON.stringify(defaultUsers));
    }
    if (!localStorage.getItem("inventory")) {
        const defaultItems = [
            { id: 1, name: "Laptop Stand", category: "Accessories", quantity: 12 },
            { id: 2, name: "USB-C Hub", category: "Electronics", quantity: 5 }
        ];
        localStorage.setItem("inventory", JSON.stringify(defaultItems));
    }
}

initStorage();

function showStatus(message, isError = false) {
    const statusEl = document.getElementById("status-message");
    if (!statusEl) return;
    statusEl.textContent = message;
    statusEl.className = `mb-4 p-3 rounded text-sm font-medium ${
        isError ? "bg-red-100 text-red-700 border border-red-300" : "bg-green-100 text-green-700 border border-green-300"
    }`;
    statusEl.classList.remove("hidden");
}

// --- LOGIN PAGE LOGIC (index.html) ---
const loginForm = document.getElementById("login-form");
if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const email = document.getElementById("login-email").value.trim();
        const password = document.getElementById("login-password").value;

        const users = JSON.parse(localStorage.getItem("users")) || [];
        const user = users.find(u => u.email === email && u.password === password);

        if (user) {
            localStorage.setItem("currentUser", JSON.stringify(user));
            window.location.href = "dashboard.html";
        } else {
            showStatus("Invalid email or password!", true);
        }
    });
}

// --- REGISTRATION PAGE LOGIC (register.html) ---
const registerForm = document.getElementById("register-form");
if (registerForm) {
    registerForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const fullname = document.getElementById("reg-fullname").value.trim();
        const email = document.getElementById("reg-email").value.trim();
        const password = document.getElementById("reg-password").value;

        const users = JSON.parse(localStorage.getItem("users")) || [];
        if (users.some(u => u.email === email)) {
            showStatus("Email already registered!", true);
            return;
        }

        users.push({ fullname, email, password });
        localStorage.setItem("users", JSON.stringify(users));
        showStatus("Registration Successful! Redirecting to login...", false);

        setTimeout(() => {
            window.location.href = "index.html";
        }, 1200);
    });
}

// --- DASHBOARD PAGE LOGIC (dashboard.html) ---
const addItemForm = document.getElementById("add-item-form");
if (addItemForm) {
    // Protect dashboard route
    const currentUser = JSON.parse(localStorage.getItem("currentUser"));
    if (!currentUser) {
        window.location.href = "index.html";
    } else {
        const welcomeEl = document.getElementById("welcome-user");
        if (welcomeEl) welcomeEl.textContent = `Welcome, ${currentUser.fullname}`;
    }

    // Logout button
    const logoutBtn = document.getElementById("logout-btn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", function () {
            localStorage.removeItem("currentUser");
            window.location.href = "index.html";
        });
    }

    // Render inventory table
    function renderInventory() {
        const tbody = document.getElementById("inventory-list");
        const items = JSON.parse(localStorage.getItem("inventory")) || [];
        tbody.innerHTML = "";

        if (items.length === 0) {
            tbody.innerHTML = `<tr><td colspan="4" class="text-center py-4 text-gray-500">No items in inventory.</td></tr>`;
            return;
        }

        items.forEach(item => {
            const tr = document.createElement("tr");
            tr.className = "border-b hover:bg-gray-50";
            tr.innerHTML = `
                <td class="py-3 px-4 font-medium text-gray-800">${item.name}</td>
                <td class="py-3 px-4 text-gray-600">${item.category}</td>
                <td class="py-3 px-4 font-semibold text-blue-600 item-qty">${item.quantity}</td>
                <td class="py-3 px-4 space-x-2">
                    <button onclick="removeOne(${item.id})" class="remove-btn bg-amber-500 hover:bg-amber-600 text-white text-xs px-3 py-1.5 rounded">
                        Remove 1
                    </button>
                    <button onclick="deleteItem(${item.id})" class="delete-btn bg-red-600 hover:bg-red-700 text-white text-xs px-3 py-1.5 rounded">
                        Delete
                    </button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    // Add item
    addItemForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("item-name").value.trim();
        const category = document.getElementById("item-category").value.trim();
        const quantity = parseInt(document.getElementById("item-quantity").value, 10);

        const items = JSON.parse(localStorage.getItem("inventory")) || [];
        const newItem = {
            id: Date.now(),
            name,
            category,
            quantity: isNaN(quantity) || quantity < 1 ? 1 : quantity
        };
        items.push(newItem);
        localStorage.setItem("inventory", JSON.stringify(items));

        addItemForm.reset();
        renderInventory();
        showStatus(`Added "${name}" to inventory!`, false);
    });

    // Remove 1 quantity
    window.removeOne = function (id) {
        let items = JSON.parse(localStorage.getItem("inventory")) || [];
        items = items.map(item => {
            if (item.id === id) {
                return { ...item, quantity: Math.max(0, item.quantity - 1) };
            }
            return item;
        }).filter(item => item.quantity > 0);

        localStorage.setItem("inventory", JSON.stringify(items));
        renderInventory();
        showStatus("Removed 1 unit from item.", false);
    };

    // Delete entire item
    window.deleteItem = function (id) {
        let items = JSON.parse(localStorage.getItem("inventory")) || [];
        items = items.filter(item => item.id !== id);
        localStorage.setItem("inventory", JSON.stringify(items));
        renderInventory();
        showStatus("Item deleted from inventory.", false);
    };

    renderInventory();
}
