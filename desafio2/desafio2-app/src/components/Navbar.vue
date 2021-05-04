<template>
  <nav class="dashuser-view navbar navbar-expand-lg sticky-top">
    <div class="container-fluid">
      <div class="row text-center">
        <div class="col-4">
          <button id="sidebarCollapse" class="btn btn-primary" @click="active_sidebar()">
            <img src="/toggler.png" alt="">
          </button>
        </div>
        <div class="col-8">
          <a class="navbar-brand text-white" href="#">
            <img src="/logo-thing.png" alt="">
          </a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    active_sidebar() {
      $('#sidebar').toggleClass('active');
      $('')
    }
  },
}
</script>

<style scoped>

</style>