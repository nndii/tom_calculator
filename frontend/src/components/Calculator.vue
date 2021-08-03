<template>
  <div id="calculator">
    <h1>Tom's Calculator</h1>
    <form @submit.prevent="processForm">
      <fieldset>
        <legend>Type Price, Quantity and State Code.</legend>
        <div class="row">
          <div class="col-sm-3 col-md-3">
            <label for="Price">Price</label>
            <input
              type="number"
              step="0.01"
              id="Price"
              placeholder="Price"
              name="price"
              v-model="price"
            />
          </div>
          <div class="col-sm-3 col-md-3">
            <label for="Quantity">Quantity</label>
            <input
              type="number"
              step="0.01"
              id="Quantity"
              placeholder="Quantity"
              name="quantity"
              v-model="quantity"
            />
          </div>
          <div class="col-sm-3 col-md-3">
            <label for="stateCode">State Code</label>
            <input
              type="text"
              id="stateCode"
              placeholder="State Code"
              name="stateCode"
              v-model="stateCode"
            />
          </div>
          <div class="col-sm-3 col-md-3">
            <button>Get Total</button>
          </div>
        </div>
      </fieldset>
    </form>
  <div id="total" class="row">
    <div class="card">
      <h3>Order total</h3>
      <p>{{ total }}</p>
    </div>
    <div class="card">
      <h3>Order total (tax incl.)</h3>
      <p>{{ tax_total }}</p>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  el: "#calculator",
  name: "Calculator",
  data: function () {
    return {
      price: "",
      quantity: "",
      stateCode: "AL",
      total: "TBC",
      tax_total: "TBC"
    }
  },
  methods: {
    processForm: function() {
      axios.post("/calculator", {
        price: this.price,
        quantity: this.quantity,
        state_code: this.stateCode
      }).then(
        (response) => {
          this.total = response.data.discounted_total
          this.tax_total = response.data.total
          console.log(response.data)
        },
        (error) => {
          alert(JSON.stringify(error.response.data))
        }
      )
    },
  },
};
</script>

<style scoped>
#total {
  display: flex;
  justify-content: center;
}
</style>
