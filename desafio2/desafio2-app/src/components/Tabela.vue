<template>
  <div class="row g-3 mb-4 justify-content-end">
    <div class="col-lg-4">
      <label for="filtro_dados">Filtro dos Dados</label>
      <select id="filtro_dados" @change="onNewFilter($event)" class="form-select" aria-label="Nº de Itens por Página">
        <option value="demanda">Demanda</option>
        <option value="capacidade">Capacidade</option>
        <option value="atendPlan">Atendimento Planejado</option>
        <option value="atendReal">Atendimento Realizado</option>
        <option value="desvio">Desvio</option>
        <option value="capXatendReal" selected>Capacidade x Atendimento Real.</option>
      </select>
    </div>
  </div>

  <!--  Gráfico dos Dados da Tabela -->
  <Grafico :data="sortedRows" :filtro="filter"></Grafico>

  <!--  Corpo da Tabela -->
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
      <tr>
        <th scope="col">
          Data
          <span class="sort arrow-down" @click="sort($event, 'data')"></span>
        </th>
        <th scope="col">
          Demanda
          <span class="sort arrow-down" @click="sort($event, 'demanda')"></span>
        </th>
        <th scope="col">
          Capacidade
          <span class="sort arrow-down" @click="sort($event, 'capacidade')"></span>
        </th>
        <th scope="col">
          Atendimento Planejado
          <span class="sort arrow-down" @click="sort($event, 'atendPlan')"></span>
        </th>
        <th scope="col">
          Atendimento Realizado
          <span class="sort arrow-down" @click="sort($event, 'atendReal')"></span>
        </th>
        <th scope="col">
          Desvio
          <span class="sort arrow-down" @click="sort($event, 'desvio')"></span>
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(row, i) in sortedRows" :key="i">
        <td>{{ row.data }}</td>
        <td>{{ row.demanda }}</td>
        <td>{{ row.capacidade }}</td>
        <td>{{ row.atendPlan }}</td>
        <td>{{ row.atendReal }}</td>
        <td>{{ row.desvio }}</td>
      </tr>
      </tbody>
    </table>
  </div>

  <!--  Controles da Tabela -->
  <div class="row justify-content-between my-3 my-md-0 mb-lg-4 table-control">
    <!-- Controles das Páginas -->
    <div class="col-6 col-md-3 col-lg-3 text-start">
      <div class="page-control" @click="prevPage">
        <svg class="bi" width="12" height="12">
          <use xlink:href="#previous-page"/>
        </svg>
      </div>
      <span class="mark-page rounded"> {{ currentPage }} </span> de {{ pageCount }}
      <div class="page-control" @click="nextPage">
        <svg class="bi" width="12" height="12">
          <use xlink:href="#next-page"/>
        </svg>
      </div>
    </div>

    <!-- Controles da Qtd. de Usuários por Página -->
    <div class="col-6 col-md-4 col-lg-4 text-end">
      <select @change="onNewValue($event)" class="form-select" aria-label="Nº de Itens por Página">
        <option value="5" selected>5</option>
        <option value="7">7</option>
        <option value="10">10</option>
      </select>
      linhas por página
    </div>
  </div>
</template>

<script>
import Grafico from "../components/Grafico.vue";

export default {
  name: "Tabela",
  components: {Grafico},
  props: {
    data: {
      type: Array,
      default: []
    },
  },
  data() {
    return {
      sort_dir: 'desc',
      currentSort: '',
      currentSortDir: 'desc',
      pageSize: 5,
      currentPage: 1,
      sort_arrows: {
        'asc': 'arrow-up',
        'desc': 'arrow-down'
      },
      graph_filter: "capXatendReal"
    }
  },
  methods: {
    sort(event, s) {
      if (s === this.currentSort) {
        $(event.target).removeClass(this.sort_arrows[this.currentSortDir])
        this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
        $(event.target).addClass(this.sort_arrows[this.currentSortDir])
      }
      this.currentSort = s;
    },
    nextPage() {
      if ((this.currentPage * this.pageSize) < this.data.length)
        this.currentPage++;
      console.log(this.currentPage)
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
      console.log(this.currentPage)
    },
    onNewValue(event) {
      this.pageSize = event.target.value
      if (this.currentPage > this.pageCount)
        this.currentPage = 1
    },
    onNewFilter(event) {
      this.graph_filter = event.target.value
    }
  },
  computed: {
    sortedRows() {
      /* Retorna o array ordenado asc ou desc
      * de acordo ao que o usuario selecionar
      **/
      return this.data.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === 'desc') modifier = -1;
        if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if (a[this.currentSort] > b[this.currentSort]) return modifier;
        return 0;
      }).filter((row, index) => {
        let start = (this.currentPage - 1) * this.pageSize;
        let end = this.currentPage * this.pageSize;
        if (index >= start && index < end) return true;
      });
    },
    pageCount() {
      return Math.floor(this.data.length / this.pageSize) + 1
    },
    filter() {
      return this.graph_filter
    }
  }
}
</script>

<style lang="sass" scoped>
@import "./src/assets/style/variables.sass"

td, th
  text-align: center

.table
  .sort
    padding-right: 15px
    height: 7px
    background-size: contain !important
    cursor: pointer

  .arrow-down
    background: url("/sort-down.png") right center no-repeat

  .arrow-up
    background: url("/sort-up.png") right center no-repeat

.page-control
  cursor: pointer
  display: inline-block

.table-control
  font-size: 13.4px
  color: $gray-font

  .act-icon
    cursor: pointer

  span
    &.mark-page
      border: 1px solid $input-border
      margin: auto 5px
      padding: 3px 15px
      background-color: inherit
      min-width: 40px
      height: 30px
      text-align: center

  select
    width: 60px
    height: 30px
    display: inline-block
    font-family: inherit
    font-size: inherit
    color: inherit
    line-height: 1.2
    padding-right: 0
    padding-left: 5px

</style>