import Vue from 'vue'
import Router from 'vue-router'
import FlashCard from './views/FlashCard.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'flashCard',
      component: FlashCard
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/vocabulary',
      name: 'vocabulary',
      component: () => import('./views/VocabularyList.vue')
    }
  ]
})
