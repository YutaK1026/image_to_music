import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home' // ★★★追加★★★

Vue.use(Router)

export default new Router({
  // パス末尾へ'#'が追加されるのを防ぐ
  mode: 'history', // ★★★追加★★★
  routes: [
    {
      // '/'に対して、frontend/src/components/ 配下のHelloWorld.vueファイルを参照する
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      // '/home'に対して、frontend/src/components/ 配下のHome.vueファイルを参照する
      path: '/home',
      name: 'Home',
      component: Home
    }
  ]
})
