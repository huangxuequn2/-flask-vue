<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>

export default {
  name: 'Ping',
  data() {
    return {
      msg: ''
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      try {
        let result = await this.$API.reqPing()
        this.msg = result
      } catch(error) {
        return Promise.reject(new Error('fail'))
      }
    },
  }
}
</script>

<style>

</style>