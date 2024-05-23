document.addEventListener("alpine:init", () => {
  console.log("baby");
  Alpine.data("dashboard", () => ({
    drawerOpen: false,
    profileOptionsOpen: false,
    user_products: [],
    setEditProductItem() {},
    showEditProductModal: false,
  }));
});
