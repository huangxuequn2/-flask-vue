import Vue from 'vue'
import App from './App.vue'
// 引入路由
import router from '@/router'
// 引入统一接口api文件夹里面的请求函数
import * as API from '@/api'
// 引入bootstrap4样式
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  // 全局事件总线
  beforeCreate() {
    Vue.prototype.$bus = this
    Vue.prototype.$API = API
  }
}).$mount('#app')
