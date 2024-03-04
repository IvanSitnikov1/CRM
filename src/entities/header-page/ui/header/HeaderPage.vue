<template>
  <div class="wrapper wrapper_title">
    <Header
      :data="{
      title: getHeaderTitle
    }"
    />
  </div>
</template>

<script setup lang="ts">
import { Header } from '@/shared/ui/header'

type ConfigItem = { route: string; title: string }
const config: ConfigItem[] = [
  { route: 'home', title: 'Dashboard' },
  { route: 'nears-events', title: 'Dashboard' },
  { route: 'calendar', title: 'Calendar' },
  { route: 'projects', title: 'Projects' },
  { route: 'vacations', title: 'Vacations' },
  { route: 'employees', title: 'Employees' },
  { route: 'messenger', title: 'Messenger' },
  { route: 'profile', title: 'Profile' },
  { route: 'my-profile', title: 'My Profile' },
]

const getHeaderTitle = computed(() =>{
  const router = useRouter()
  const currentRoute = router.currentRoute.value.name
  const titleConfig = config.find(item => item.route === currentRoute)

  return titleConfig?.title ?? 'Error'
})
</script>
