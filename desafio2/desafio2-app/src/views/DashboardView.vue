<template>
  <h4>Home Dashboard</h4>
  <div class="container mt-4">
    <Tabela :data="rows"></Tabela>
  </div>
</template>

<script>
import Grafico from "../components/Grafico.vue";
import Tabela from "../components/Tabela.vue";

export default {
  name: "DashboardView",
  components: {Grafico, Tabela},
  data() {
    return {
      rows: [
        {
          data: "10/01/2020",
          demanda: 20,
          capacidade: 10,
          atendPlan: 41,
          atendReal: 10,
          desvio: 15
        },
        {
          data: "11/02/2020",
          demanda: 12,
          capacidade: 19,
          atendPlan: 42,
          atendReal: 10,
          desvio: 25
        },
        {
          data: "12/03/2020",
          demanda: 20,
          capacidade: 12,
          atendPlan: 43,
          atendReal: 10,
          desvio: 18
        },
        {
          data: "13/04/2020",
          demanda: 6,
          capacidade: 52,
          atendPlan: 44,
          atendReal: 10,
          desvio: 18
        },
        {
          data: "14/05/2020",
          demanda: 20,
          capacidade: 12,
          atendPlan: 45,
          atendReal: 10,
          desvio: 18
        },
        {
          data: "15/06/2020",
          demanda: 25,
          capacidade: 46,
          atendPlan: 46,
          atendReal: 10,
          desvio: 18
        },
        {
          data: "16/07/2020",
          demanda: 35,
          capacidade: 12,
          atendPlan: 47,
          atendReal: 10,
          desvio: 18
        },
        {
          data: "17/08/2020",
          demanda: 36,
          capacidade: 13,
          atendPlan: 48,
          atendReal: 11,
          desvio: 58
        }
      ],
    }
  }
}
</script>

<style scoped>

</style>