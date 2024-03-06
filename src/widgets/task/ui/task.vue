<template>
    <Title
        class="wrapper wrapper_title"
        :data="{
            title: data.taskName,
        }"
    />
    <div class="wrapper">
        <article class="task-description">
            <header class="task-description__header">
                <template v-if="data.type === 'info'">
                    <Title
                        :data="{
                            title: 'Task info',
                            size: 'small',
                            isHighLeading: true,

                        }"
                    />
                </template>
                <template v-else>
                    <div>
                        in review
                    </div>
                    <ActionEdit />
                </template>
            </header>
            <main>
                <template v-for="(section, index) in data.sections">
                    <div
                        v-if="section.type === 'about'"
                        :key="index"
                        class="task-description__about"
                    >
                        <Title
                            :data="{
                                title: 'Description',
                                size: 'small',
                                marginBottom: 'small',
                                isHighLeading: true,
                            }"
                        />
                        <p class="task-description__description">
                            {{ section.description }}
                        </p>
                    </div>
                    <div
                        :key="index + 1"
                        v-else-if="section.type === 'number'"
                        class="task-description__number"
                    >
                        <span class="task-description__title"> {{ section.title }}</span>
                        <span class="task-description__id">{{ section.id }}</span>
                    </div>
                    <div
                        :key="index + 2"
                        v-else-if="section.type === 'info'"
                        class="task-description__info"
                    >
                        <div class="task-description__reporter">
                            <span class="task-description__column-name">Reporter</span>
                            <TagUser
                                :data="{
                                    fullName: 'Blake Maxwell',
                                    image: '',
                                }"
                            />
                        </div>
                        <div class="task-description__assignees">
                            <span class="task-description__column-name">Assignees</span>
                            <Avatars :data="{}" />
                        </div>
                        <div class="task-description__priority">
                            <span class="task-description__column-name">Priority</span>
                            <Priority
                                :data="{
                                    priority: 'medium',
                                    isShowText: true,
                                }"
                            />
                        </div>
                        <div class="task-description__deadline">
                            <span class="task-description__column-name">Dead Line</span>
                            <time class="task-description__deadline-data">Feb 23, 2020</time>
                        </div>
                    </div>
                    <div
                        :key="index + 3"
                        v-else-if="section.type === 'time'"
                        class="task-description__time"
                    >
                        <Title
                            :data="{
                                title: 'Time tracing',
                                size: 'medium',
                                marginBottom: 'medium',
                                isHighLeading: true,
                            }"
                        />
                        <div class="task-description__log-time">
                            <CircleProgressBar
                                :data="{
                                    value: section.timeLog,
                                    max: section.timeMax,
                                    size: 40,
                                }"
                            />
                            <div class="task-description__text-time">
                                <Title
                                    :data="{
                                        title: `${section.timeLog} logged`,
                                        size: 'small',
                                    }"
                                />
                                <span>Original Estimate {{ section.timeMax }}</span>
                            </div>
                        </div>
                        <UiButton
                            :data="{
                                title: 'Log time',
                                type: 'button',
                                isFull: true,
                                iconNameLeft: 'clock',
                            }"
                        />
                    </div>
                    <div
                        :key="index + 4"
                        v-else-if="section.type === 'created'"
                        class="task-description__created"
                    >
                        <IconBase
                            :data="{
                                iconName: 'calendar',
                            }"
                        />
                        <time class="task-description__created-data">
                            {{ section.createdDate }}
                        </time>
                    </div>
                </template>
            </main>
            <footer
                v-if="data.type !== 'info'"
                class="task-description__footer"
            >
                <div class="task-description__actions">
                    <ActionAddFile />
                    <ActionCreatLink />
                </div>
            </footer>
        </article>
    </div>
</template>

<script setup lang="ts">
import { CircleProgressBar } from '@/shared/ui/circle-progress-bar';
import { Priority } from '@/shared/ui/priority';
import { Avatars } from '@/shared/ui/avatars';
import { UiButton } from '@/shared/ui/button';
import { IconBase } from '@/shared/ui/icon-base';
import { Title } from '@/shared/ui/title';
import { TagUser } from '@/shared/ui/tag-user';
import { ActionCreatLink } from '@/features/creat-link';
import { ActionAddFile } from '@/features/add-file';
import { ActionEdit } from '@/features/edit';

const data = {
  taskName: 'Sample Task',
  type: 'info',
  sections: [
    {
      type: 'number',
      title: 'Task Number',
      id: '#123'
    },
    {
      type: 'about',
      description: 'This is a sample task-description description.'
    },
    {
      type: 'info',
      reporter: {
        fullName: 'John Doe',
        image: ''
      },
      assignees: [],
      priority: 'high',
      deadline: 'Feb 23, 2024'
    },
    {
      type: 'time',
      timeLog: 20,
      timeMax: 40
    },
    {
      type: 'created',
      createdDate: 'Feb 22, 2024'
    }
  ]
};

</script>

<style lang="scss">
  @import "style.module";
</style>
