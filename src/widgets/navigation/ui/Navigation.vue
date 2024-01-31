<template>
  <teleport to="body">
    <transition name="navigation">
      <aside  v-if="app.showNavigation" class="navigation" @keyup.esc="closeNavigation" @click.self="closeNavigation" >
        <div class="navigation__container">
          <NavigationToggle class="navigation__logo"/>
          <nav class="navigation__nav">
            <ul class="navigation__menu">
              <li class="navigation__list" v-for="(item, index) in menuItems" :key="index">
                <div class="navigation__item">
                  <img src="@/shared/assets/icons/menu.svg" alt="category">
                  <router-link class="navigation__router" :to="item.route" @click="closeNavigation">
                    {{ item.label }}
                  </router-link>
                </div>
              </li>
            </ul>
          </nav>
          <UiButton class="navigation__button" :data="{
            title: 'Support'
          }" />
          <div class="navigation__logout">
            <img src="@/shared/assets/icons/logout.svg" alt="Log out">
            <button class="navigation__button_logout">
              Log out
            </button>
          </div>
        </div>
      </aside>
    </transition>
  </teleport>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { UiButton } from '@/shared/ui/button'
import { menuItems } from '@/widgets/navigation'

const router = useRouter()

import { useAppModel } from '@/entities/app'
import { NavigationToggle } from '@/features/navigation'

const app = useAppModel()


const closeNavigation = () => {
  app.updateShowMenu(false)
};
</script>


<style lang="scss">
  @import "style.module";


</style>
