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

var chart = new ApexCharts(document.querySelector("#chart"), options);

chart.render();

document.addEventListener("alpine:init", async () => {
  // let response = await fetch("/dashboard/profile");
  // console.log(await response.json());
  await Alpine.data("dashboard", () => ({
    async init() {
      let response = await fetch("/dashboard/profile");
      this.user = await response.json();
      console.log(this.user);
    },
    user: null,
    drawerOpen: false,
    profileOptionsOpen: false,
    user_products: [],
    setEditProductItem() {},
    showEditProductModal: false,
    showEditWalletModal: false,
    showRequestPaymentModal: false,
  }));
});
