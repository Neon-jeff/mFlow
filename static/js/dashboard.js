var options = {
  colors: [],
  stroke: {
    curve: "smooth",
  },
  chart: {
    type: "line",
    toolbar: {
      show: false,
    },
  },
  series: [
    {
      name: "sales",
      data: [30, 40, 35, 50, 49, 60],
    },
  ],
  xaxis: {
    categories: ["jan", "feb", "mar", "apr", "may", "jun"],
  },
};

document.addEventListener("alpine:init", async () => {
  // let response = await fetch("/dashboard/profile");
  // console.log(await response.json());
  await Alpine.data("dashboard", () => ({
    async init() {
      let response = await fetch("/dashboard/profile");
      this.user = await response.json();
      var chart = new ApexCharts(document.querySelector("#chart"), options);
      chart.render();
    },
    user: {},
    drawerOpen: false,
    profileOptionsOpen: false,
    user_products: [],
    setEditProductItem() {},
    showEditProductModal: false,
    showEditWalletModal: false,
    showRequestPaymentModal: false,
    showCreateProductModal: false,
    showBaseLoader: false,
    showErrorLoader: false,
    errorText: "Something went wrong, reload and try again",
    async createProduct(e) {
      e.preventDefault();
      this.showCreateProductModal = false;
      this.showBaseLoader = true;
      let imageCounter = 0;
      let form = new FormData(document.querySelector(".create-product"));

      for (let [i, j] of form.entries()) {
        if (i == "image") {
          imageCounter++;
          form.set(`image${imageCounter}`, j);
        }
      }
      if (imageCounter !== 4) {
        this.showBaseLoader = false;
        this.errorText =
          "Upload 4 images to create a product, simply long long press an image on your phone to select multiple images";
        this.showErrorLoader = true;
        return;
      }
      form.delete("image");
      await fetch("/products/create-product/", {
        method: "post",
        body: form,
      }).then(async (res) => {
        if (!res.ok) {
          this.showBaseLoader = false;
          this.errorText = "An error occured";
          this.showErrorLoader = true;
          return;
        } else {
          this.showBaseLoader = false;
          location.reload();
        }
      });
    },
    async addProductToPromotion(id) {
      this.showBaseLoader = true;
      let form = new FormData();
      form.set("product", id);
      let res = await fetch("/dashboard/create-promotion/", {
        method: "post",
        body: form,
      });
      if (!res.ok) {
        this.errorText = "Something went wrong,try again";
        this.showBaseLoader = false;
        this.showErrorLoader = true;
        return;
      }
      this.showBaseLoader = false;
      window.location.reload();
    },
  }));
});
