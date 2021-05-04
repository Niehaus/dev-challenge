<template>
  <h5 class="text-center"> {{ dataPortion[filtro] }} </h5>
  <div id="chartDiv"></div>
</template>

<script>
import * as JSC from "jscharting";

export default {
  name: "Grafico",
  props: {
    data: {
      type: Array,
      default: []
    },
    filtro: {
      type: String,
      default: "capXatendReal"
    }
  },
  data() {
    return {
      dataPortion: {
        "demanda": 'Demanda',
        "capacidade": 'Capacidade',
        "atendPlan": 'Atendimento Planejado',
        "atendReal": 'Atendimento Real',
        "desvio": 'Desvio',
        "capXatendReal": 'Relação Capacidade x Atendimento Realizado'
      },
      dataFormatMap: {
        "01": 'Jan',
        "02": 'Fev',
        "03": 'Marc',
        "04": 'Abr',
        "05": 'Maio',
        "06": 'Jun',
        "07": 'Jul',
        "08": 'Ago',
        "09": 'Set',
        "10": 'Out',
        "11": 'Nov',
        "12": 'Dez',
      }
    }
  },
  created() {
    // Remount no grafico qd alterar data
    this.$watch(
        () => this.data + this.filtro,
        () => {
          this.mountGrafico();
        }
    );
  },
  methods: {
    mountGrafico() {
      JSC.chart('chartDiv', {
        debug: true,
        defaultSeries_type: 'column',
        series: [
          {
            name: this.dataPortion[this.filtro],
            hatchPalette: true,
            defaultPoint_hatch_color: '#000',
            palette: 'default',
            points: this.processedPoints
          }
        ]
      });
    },
    dataFormat(data) {
      // Mapeia o número do mês p/ seu nome
      let formated = data.split('/'),
          dia = formated[0], ano = formated[2],
          mes = this.dataFormatMap[formated[1]]

      return `${dia} ${mes} ${ano}`
    }
  },
  computed: {
    processedPoints() {
      // Render do grafico de acordo ao filtro de dados
      let gpoints = [], relacao
      this.data.forEach(point => {
        switch (this.filtro) {
          case 'capXatendReal':
            relacao = point.capacidade - point.atendReal
            break
          case 'capacidade':
            relacao = point.capacidade
            break
          case 'demanda':
            relacao = point.demanda
            break
          case 'desvio':
            relacao = point.desvio
            break
          case 'atendPlan':
            relacao = point.atendPlan
            break
          case 'atendReal':
            relacao = point.atendReal
            break
        }
        gpoints.push({ name: this.dataFormat(point.data), y: relacao })
      });

      return gpoints
    }
  },
  mounted() {
    this.mountGrafico()
  }
}
</script>

<style lang="sass" scoped>
#chartDiv
  width: 100%
  height: 400px
  margin: 20px 0
</style>