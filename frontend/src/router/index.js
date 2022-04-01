import Vue from 'vue'
import Router from 'vue-router'
import ImageHome from '@/components/ImageHome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ImageHome',
      component: ImageHome
    }
  ]
})
