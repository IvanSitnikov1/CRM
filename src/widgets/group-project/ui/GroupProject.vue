<template>
    <Collapse
        @onExpanded="handlerExpandedGroup"
        :data="{ isExpanded: state.expendedGrope }"
    >
        <template #header>
            <div
                class="group-project__group"
                :class="{ 'group-project__group_active': !state.expendedGrope }"
            >
                <Title
                    class="group-project__group-name"
                    :class="{ 'group-project__group-name_active': !state.expendedGrope }"
                    :data="{ title: 'Active Tasks', size: 'small', isHighLeading: true }"
                />
            </div>
        </template>
        <template #content>
            <div class="group-project__inner-groups">
                <Collapse
                    @onExpanded="handlerExpandedTask(index)"
                    v-for="(tasks, index) in state.taskData.allTasks"
                    :key="index"
                    :data="{
                        isExpanded: state.expendedTasks.has(index),
                        title: tasks.title,
                    }"
                >
                    <template #content>
                        <div class="group-project__tasks">
                            <CardTask
                                v-for="task in tasks"
                                :key="task.id"
                                :data="task"
                            />
                        </div>
                    </template>
                </Collapse>
            </div>
        </template>
    </Collapse>
</template>

<script setup lang="ts">
import { Collapse } from '@/shared/ui/collaps';
import { Title } from '@/shared/ui/title';
import { CardTask } from '@/entities/task';

const state = reactive({
  expendedGrope: true,
  expendedTasks: new Set(),
  // todo: Выпелить отсюда и получать с сервера
  taskData: {
    allTasks: [{
      title: 'Development (5 issues)',
      tasks: Array.from({ length: 5 }, (_, index) => ({
        id: index + 1,
        title: `Development Task ${index + 1}`
      }))
    },
    {
      title: 'Design (2 issues)',
      tasks: Array.from({ length: 2 }, (_, index) => ({
        id: index + 1,
        title: `Design Task ${index + 1}`
      }))
    }]
  }
});

const handlerExpandedGroup = value => {
  state.expendedGrope = value;
};

const handlerExpandedTask = value => {
  if (state.expendedTasks.has((value))) {
    state.expendedTasks.delete(value);
  } else {
    state.expendedTasks.add(value);
  }
};
</script>

<style scoped lang="scss">
  @import "style.module";
</style>
