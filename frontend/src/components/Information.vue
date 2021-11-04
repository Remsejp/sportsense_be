<template>
  <h1 style="text-align: center">
    ¡Bienvenido Informacion <span> {{ username }} </span>!
  </h1>
  <br />
  <br />
  <div class="container">
    <div class="row">
      <div class="col"><img src="@/assets/logo.png" /></div>
      <div class="col">
        <p class="fst-italic">
          En Antioquia y el Eje Cafetero, se le dice a los pequeños
          establecimientos de barrio, que comercializan generalmente frutas y
          verduras, y en menor medida otros víveres.
        </p>
      </div>
      <div class="col"><img src="@/assets/revuelto.jpg" /></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Information",
  data: function () {
    return {
      username: localStorage.getItem("username") || "none",
    };
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