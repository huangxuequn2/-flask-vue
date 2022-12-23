import Vue from 'vue'
import VueRouter from 'vue-router'

import Ping from '@/components/Ping'

// 注册路由
Vue.use(VueRouter)

// 对外暴露路由
export default new VueRouter({
    routes: [
        {
            name: 'ping',
            path: '/',
            component: Ping
        }
    ]
})