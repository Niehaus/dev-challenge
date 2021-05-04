<template>
  <div class="wrapper">
    <!-- Sidebar  -->
    <nav id="sidebar" class="active">
      <div class="sidebar-header">
        <div class="row justify-content-center">
          <h6 class="text-center fw-bold">Desafio 2</h6>
        </div>
      </div>
      <slot name="sidebar-list"></slot>
    </nav>
    <!-- Page Content  -->
    <div id="content">
      <slot name="page-content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  props: {
  },
  data() {
    return {
      profile_pic: {
        type: Boolean
      }
    }
  },
  methods: {
    sidebar_interact() {
      /**
       * Interação com os menus da side bar
       * -> jquery events
       */
      let side_li = $('#sidebar  ul > li')
      side_li.on("click", function () {
        if (!$(this).hasClass('collap')) {
          for (let i = 0; i < side_li.length; i++) {
            if ($(side_li[i]).hasClass('active'))
              $(side_li[i]).removeClass('active')
          }
          $(this).addClass('active')
        }
      });
    }
  },
  mounted() {
    this.sidebar_interact()
  }
}
</script>

<style lang="sass">
@import "./src/assets/style/sidebar.sass"

.outer-icon
  .li-title
    font-size: 15px

</style>