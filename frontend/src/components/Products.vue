<template>
  <h1 style="text-align: center">
    ¡Bienvenido Productos <span> {{ username }} </span>!
  </h1>
  <br />
  <br />
  <div class="container">
    <div class="row">
      <div class="col">
        <h2>crear</h2>
        <form v-on:submit.prevent="processCreate">
          <input
            type="text"
            class="form-control"
            v-model="elementP.name"
            placeholder="Nombre producto"
          />
          <br />
          <input
            type="number"
            class="form-control"
            v-model="elementP.price"
            placeholder="Precio"
          />
          <br />
          <br />
          <button type="submit" class="btn btn-primary">Crear</button>
        </form>
      </div>
      <div class="col">
        <h2>Consular</h2>
        <form v-on:submit.prevent="processGetProduct">
          <input
            type="text"
            class="form-control"
            v-model="elementP.id"
            placeholder="Ingrese ID Producto"
          />
          <br />
          <p style="text-align: center">
            <span> {{ onlyOneP.name }} </span>
            <br />
            <span> {{ onlyOneP.price }} </span>
          </p>
          <br />
          <button type="submit" class="btn btn-primary">Consular</button>
        </form>
      </div>
      <div class="col">
        <h2>Actualizar</h2>
        <form v-on:submit.prevent="processUpgrade">
          <input
            type="text"
            class="form-control"
            v-model="elementP.id"
            placeholder="Ingrese ID Producto"
          />
          <br />
          <input
            type="text"
            class="form-control"
            v-model="elementP.name"
            placeholder="Nombre"
          />
          <br />
          <input
            type="number"
            class="form-control"
            v-model="elementP.price"
            placeholder="Precio"
          />
          <br />
          <br />
          <button type="submit" class="btn btn-primary">Modificar</button>
        </form>
      </div>
      <div class="col">
        <h2>Borrar</h2>
        <form v-on:submit.prevent="processDelete">
          <input
            type="text"
            class="form-control"
            v-model="elementP.id"
            placeholder="Ingrese ID Producto"
          />
          <br />
          <br />
          <button type="submit" class="btn btn-primary">Borrar</button>
        </form>
      </div>
    </div>
  </div>
  <br />
  <br />
  <button class="btn btn-secondary" v-on:click="processData">Actualizar tabla</button>
  <table class="table">
    <thead>
      <tr>
        <th>Name</th>
        <th>price</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="product in products" :key="product.id">
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "Products",
  data: function () {
    return {
      username: localStorage.getItem("username") || "none",
      products: [],
      elementP: {
        id: "",
        name: "",
        price: 0,
      },
      onlyOneP: {
        name: "",
        price: 0,
      },
    };
  },
  methods: {
    processData: function () {
      axios
        .get("https://sportsense.herokuapp.com/productos/", {
          headers: {},
        })
        .then((result) => {
          console.log(result.data);
          this.products = result.data;
        })
        .catch((error) => {
          alert(error);
        });
    },
    processCreate: function () {
      axios
        .post(
          "https://sportsense.herokuapp.com/productos/",
          this.elementP,
          {
            headers: {},
          }
        )
        .then((result) => {
          alert(result.status + " Creado exitosamente..");
        })
        .catch((error) => {
          alert(error);
        });
    },
    processGetProduct: function () {
      axios
        .get(
          `https://http://sportsense.herokuapp.com/busquedad_productos/${this.elementP.id}`,
          this.elementP,
          {
            headers: {},
          }
        )
        .then((result) => {
          this.onlyOneP.name = result.data.name;
          this.onlyOneP.price = result.data.price;
        })
        .catch((error) => {
          alert(error);
        });
    },
    processUpgrade: function () {
      axios
        .put(
          `https://http://sportsense.herokuapp.com/busquedad_productos/${this.elementP.id}`,
          this.elementP,
          {
            headers: {},
          }
        )
        .then((result) => {
          alert(result.status + " Actualizado exitosamente..");
        })
        .catch((error) => {
          alert(error);
        });
    },
    processDelete: function () {
      axios
        .delete(
          `https://http://sportsense.herokuapp.com/busquedad_productos/${this.elementP.id}`,
          {
            headers: {},
          }
        )
        .then((result) => {
          alert(result.status + " Borrado exitosamente..");
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
  created: function () {
    this.processData();
  },
};
</script>
<style>
h1 {
  font-size: 50px;
  color: #283747;
}
span {
  color: crimson;
  font-weight: bold;
}
</style>