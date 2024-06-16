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
      let form = new FormData(document.querySelector(".create-product"));
      console.log(form.entries().next());
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
  }));
});
