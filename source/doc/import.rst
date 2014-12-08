==============
TEST-TEST-TEST
==============
JUST TESTING

TEST?TEST?TEST?
---------------


.. code-block:: php

    class ImportSourceEvent
    {
        /**
         * @var test
         */
        protected $test;

        /**
         * @param EntityManager $manager
         * @param string        $Class
         * @param Manager       $Manager
         * @param string        $documentClass
         */
        public function __construct(EntityManager $manager, $Class, Manager $Manager, $documentClass)
        {
            $this->entityManager = $manager;
        }

        /**
         * Gets data and adds source.
         *
         * @param TestEvent $event
         */
        public function onSource(TestEvent $event)
        {
            $event->addSource($this->getAllDocuments());
        }
    }

..

TESTS

.. code-block:: yml

    my.import.source:
           class: %my.import.source.class%
           parent: my.import.source
           arguments:
             - %my.entity.class%
           tags:
             - { name: kernel.event_listener, event: import.default.source, method: onSource }

..
