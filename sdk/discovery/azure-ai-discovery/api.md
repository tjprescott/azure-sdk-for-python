```py
namespace azure.ai.discovery

    class azure.ai.discovery.BookshelfClient(_GeneratedBookshelfClient): implements ContextManager 
        knowledge_base_versions: KnowledgeBaseVersionsOperations
        knowledge_bases: KnowledgeBasesOperations

        def __init__(
                self, 
                endpoint: str, 
                credential: TokenCredential, 
                *, 
                api_version: Optional[str] = ..., 
                transport: Optional[HttpTransport] = ..., 
                **kwargs: Any
            ) -> None: ...

        def close(self) -> None: ...

        def send_request(
                self, 
                request: HttpRequest, 
                *, 
                stream: bool = False, 
                **kwargs: Any
            ) -> HttpResponse: ...


    class azure.ai.discovery.WorkspaceClient(_GeneratedWorkspaceClient): implements ContextManager 
        conversations: ConversationsOperations
        investigations: InvestigationsOperations
        tasks: TasksOperations
        tools: ToolsOperations

        def __init__(
                self, 
                endpoint: str, 
                credential: TokenCredential, 
                *, 
                api_version: Optional[str] = ..., 
                transport: Optional[HttpTransport] = ..., 
                **kwargs: Any
            ) -> None: ...

        def close(self) -> None: ...

        def send_request(
                self, 
                request: HttpRequest, 
                *, 
                stream: bool = False, 
                **kwargs: Any
            ) -> HttpResponse: ...


namespace azure.ai.discovery.aio

    class azure.ai.discovery.aio.BookshelfClient(_GeneratedBookshelfClient): implements AsyncContextManager 
        knowledge_base_versions: KnowledgeBaseVersionsOperations
        knowledge_bases: KnowledgeBasesOperations

        def __init__(
                self, 
                endpoint: str, 
                credential: AsyncTokenCredential, 
                *, 
                api_version: Optional[str] = ..., 
                transport: Optional[AsyncHttpTransport] = ..., 
                **kwargs: Any
            ) -> None: ...

        async def close(self) -> None: ...

        def send_request(
                self, 
                request: HttpRequest, 
                *, 
                stream: bool = False, 
                **kwargs: Any
            ) -> Awaitable[AsyncHttpResponse]: ...


    class azure.ai.discovery.aio.WorkspaceClient(_GeneratedWorkspaceClient): implements AsyncContextManager 
        conversations: ConversationsOperations
        investigations: InvestigationsOperations
        tasks: TasksOperations
        tools: ToolsOperations

        def __init__(
                self, 
                endpoint: str, 
                credential: AsyncTokenCredential, 
                *, 
                api_version: Optional[str] = ..., 
                transport: Optional[AsyncHttpTransport] = ..., 
                **kwargs: Any
            ) -> None: ...

        async def close(self) -> None: ...

        def send_request(
                self, 
                request: HttpRequest, 
                *, 
                stream: bool = False, 
                **kwargs: Any
            ) -> Awaitable[AsyncHttpResponse]: ...


namespace azure.ai.discovery.models

    class azure.ai.discovery.models.ByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        APPLICATION = "Application"
        SYSTEM = "System"
        USER = "User"


    class azure.ai.discovery.models.ComputeUsage(_Model):
        supercomputers: dict[str, SupercomputerUsage]

        @overload
        def __init__(
                self, 
                *, 
                supercomputers: dict[str, SupercomputerUsage]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.Conversation(_Model):
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        display_name: Optional[str]
        investigation_name: Optional[str]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        name: str
        project_name: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                display_name: Optional[str] = ..., 
                investigation_name: Optional[str] = ..., 
                project_name: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.DiscoveryEngine(_Model):
        configuration: Optional[dict[str, Any]]
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        discovery_engine_status: Union[str, DiscoveryEngineStatus]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        system_prompt: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                configuration: Optional[dict[str, Any]] = ..., 
                discovery_engine_status: Union[str, DiscoveryEngineStatus], 
                system_prompt: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.DiscoveryEngineStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        ACTIVE = "Active"
        INACTIVE = "Inactive"


    class azure.ai.discovery.models.DiscoveryEngineUpdate(_Model):
        configuration: Optional[dict[str, Any]]
        discovery_engine_status: Optional[Union[str, DiscoveryEngineStatus]]
        system_prompt: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                configuration: Optional[dict[str, Any]] = ..., 
                discovery_engine_status: Optional[Union[str, DiscoveryEngineStatus]] = ..., 
                system_prompt: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.ExecutionHistoryEntry(_Model):
        action: str
        additional_details: Optional[dict[str, Any]]
        created_at: datetime
        created_by: str
        created_by_type: Union[str, ByType]
        response_message_id: Optional[str]
        response_message_text: Optional[str]
        summary: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                action: str, 
                additional_details: Optional[dict[str, Any]] = ..., 
                created_at: datetime, 
                created_by: str, 
                created_by_type: Union[str, ByType], 
                response_message_id: Optional[str] = ..., 
                response_message_text: Optional[str] = ..., 
                summary: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.IndexingStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        CANCELED = "Canceled"
        FAILED = "Failed"
        NOT_STARTED = "NotStarted"
        RUNNING = "Running"
        SUCCEEDED = "Succeeded"


    class azure.ai.discovery.models.InfraOverrides(_Model):
        cpu: Optional[str]
        gpu: Optional[str]
        image_uri: Optional[str]
        ram: Optional[str]
        replica_count: Optional[int]

        @overload
        def __init__(
                self, 
                *, 
                cpu: Optional[str] = ..., 
                gpu: Optional[str] = ..., 
                image_uri: Optional[str] = ..., 
                ram: Optional[str] = ..., 
                replica_count: Optional[int] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.InlineFile(_Model):
        encoded_file: str
        mount_path: str

        @overload
        def __init__(
                self, 
                *, 
                encoded_file: str, 
                mount_path: str
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.InputDataMount(_Model):
        mount_path: str
        storage_uri: str

        @overload
        def __init__(
                self, 
                *, 
                mount_path: str, 
                storage_uri: str
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.Investigation(_Model):
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        description: Optional[str]
        display_name: Optional[str]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        name: str
        project_name: str
        status: Optional[Union[str, InvestigationStatus]]
        tags: Optional[list[Tag]]

        @overload
        def __init__(
                self, 
                *, 
                description: Optional[str] = ..., 
                display_name: Optional[str] = ..., 
                tags: Optional[list[Tag]] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.InvestigationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        CREATED = "Created"
        FAILED = "Failed"
        VALIDATED = "Validated"


    class azure.ai.discovery.models.KnowledgeBase(_Model):
        bookshelf_name: str
        copilot_instruction: str
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        description: str
        id: Optional[str]
        knowledge_base_url: Optional[str]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        name: str
        provisioning_state: Optional[Union[str, ProvisioningState]]
        status: Optional[Union[str, IndexingStatus]]
        storage_asset_references: Optional[list[StorageAssetReference]]
        tags: Optional[list[Tag]]
        version: str

        @overload
        def __init__(
                self, 
                *, 
                copilot_instruction: str, 
                description: str, 
                storage_asset_references: Optional[list[StorageAssetReference]] = ..., 
                tags: Optional[list[Tag]] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.KnowledgeBaseOperationStatus(_Model):
        error: Optional[ODataV4Format]
        id: str
        result: Optional[KnowledgeBaseVersion]
        status: Union[str, OperationState]

        @overload
        def __init__(
                self, 
                *, 
                error: Optional[ODataV4Format] = ..., 
                id: str, 
                result: Optional[KnowledgeBaseVersion] = ..., 
                status: Union[str, OperationState]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.KnowledgeBaseVersion(_Model):
        bookshelf_name: str
        copilot_instruction: str
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        description: str
        id: Optional[str]
        knowledge_base_url: Optional[str]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        name: str
        provisioning_state: Optional[Union[str, ProvisioningState]]
        status: Optional[Union[str, IndexingStatus]]
        storage_asset_references: Optional[list[StorageAssetReference]]
        tags: Optional[list[Tag]]
        version: str

        @overload
        def __init__(
                self, 
                *, 
                copilot_instruction: str, 
                description: str, 
                storage_asset_references: Optional[list[StorageAssetReference]] = ..., 
                tags: Optional[list[Tag]] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.NodepoolUsage(_Model):
        allocatable_cp_us: str
        allocatable_gp_us: str
        allocatable_memory: str
        reserved_cp_us: str
        reserved_gp_us: str
        reserved_memory: str

        @overload
        def __init__(
                self, 
                *, 
                allocatable_cp_us: str, 
                allocatable_gp_us: str, 
                allocatable_memory: str, 
                reserved_cp_us: str, 
                reserved_gp_us: str, 
                reserved_memory: str
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.Operation(_Model):
        completed_at: Optional[datetime]
        created_at: datetime
        created_by: Optional[str]
        id: str
        nodepool_id: str
        runtime_details: str
        status: Union[str, RunStatus]

        @overload
        def __init__(
                self, 
                *, 
                completed_at: Optional[datetime] = ..., 
                created_at: datetime, 
                created_by: Optional[str] = ..., 
                id: str, 
                nodepool_id: str, 
                runtime_details: str, 
                status: Union[str, RunStatus]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.OperationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        CANCELED = "Canceled"
        FAILED = "Failed"
        NOT_STARTED = "NotStarted"
        RUNNING = "Running"
        SUCCEEDED = "Succeeded"


    class azure.ai.discovery.models.OperationStatusRunResultError(_Model):
        error: Optional[ODataV4Format]
        id: str
        result: Optional[RunResult]
        status: Union[str, OperationState]

        @overload
        def __init__(
                self, 
                *, 
                error: Optional[ODataV4Format] = ..., 
                id: str, 
                result: Optional[RunResult] = ..., 
                status: Union[str, OperationState]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.OutputDataMount(_Model):
        mount_path: str
        storage_uri: str

        @overload
        def __init__(
                self, 
                *, 
                mount_path: str, 
                storage_uri: str
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.OutputDataUri(_Model):
        mount_path: str
        storage_uri: str

        @overload
        def __init__(
                self, 
                *, 
                mount_path: str, 
                storage_uri: str
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.PagedOperation(_Model):
        next_link: Optional[str]
        value: list[Operation]

        @overload
        def __init__(
                self, 
                *, 
                next_link: Optional[str] = ..., 
                value: list[Operation]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.PagedWorkingMemoryEntry(_Model):
        next_link: Optional[str]
        value: list[WorkingMemoryEntry]

        @overload
        def __init__(
                self, 
                *, 
                next_link: Optional[str] = ..., 
                value: list[WorkingMemoryEntry]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        ACCEPTED = "Accepted"
        CANCELED = "Canceled"
        DELETING = "Deleting"
        FAILED = "Failed"
        PROVISIONING = "Provisioning"
        SUCCEEDED = "Succeeded"
        UPDATING = "Updating"


    class azure.ai.discovery.models.RepeatabilityResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        ACCEPTED = "accepted"
        REJECTED = "rejected"


    class azure.ai.discovery.models.ResourceOperationStatusInvestigationInvestigationError(_Model):
        error: Optional[ODataV4Format]
        id: str
        result: Optional[Investigation]
        status: Union[str, OperationState]

        @overload
        def __init__(
                self, 
                *, 
                error: Optional[ODataV4Format] = ..., 
                id: str, 
                result: Optional[Investigation] = ..., 
                status: Union[str, OperationState]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.RunRequestEnvironmentVariable(_Model):
        name: str
        value: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                name: str, 
                value: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.RunResult(_Model):
        completed_at: Optional[datetime]
        created_at: Optional[datetime]
        created_by: Optional[str]
        debug_info: str
        output_data: list[OutputDataUri]
        runtime_details: str
        status: Optional[str]
        tool_report: Optional[RunResultToolReport]

        @overload
        def __init__(
                self, 
                *, 
                created_by: Optional[str] = ..., 
                debug_info: str, 
                output_data: list[OutputDataUri], 
                runtime_details: str, 
                status: Optional[str] = ..., 
                tool_report: Optional[RunResultToolReport] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.RunResultToolReport(_Model):
        logs: Optional[str]
        percentage_complete: int
        status_information: Optional[Any]

        @overload
        def __init__(
                self, 
                *, 
                logs: Optional[str] = ..., 
                percentage_complete: int, 
                status_information: Optional[Any] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.RunStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        CANCELED = "Canceled"
        FAILED = "Failed"
        NOT_STARTED = "NotStarted"
        RUNNING = "Running"
        SUCCEEDED = "Succeeded"


    class azure.ai.discovery.models.StartTaskRequest(_Model):
        assignee: Optional[TaskAssignee]

        @overload
        def __init__(
                self, 
                *, 
                assignee: Optional[TaskAssignee] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.StorageAssetReference(_Model):
        id: str
        user_assigned_identity: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                id: str, 
                user_assigned_identity: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.SupercomputerUsage(_Model):
        active_jobs: int
        nodepools: dict[str, NodepoolUsage]
        pending_jobs: int

        @overload
        def __init__(
                self, 
                *, 
                active_jobs: int, 
                nodepools: dict[str, NodepoolUsage], 
                pending_jobs: int
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.Tag(_Model):
        key: Optional[str]
        value: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                key: Optional[str] = ..., 
                value: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.Task(_Model):
        assigned_to: Optional[TaskAssignee]
        comments: Optional[list[TaskComment]]
        created_at: Optional[datetime]
        created_by: Optional[str]
        created_by_type: Optional[Union[str, ByType]]
        depends_on: Optional[list[str]]
        description: Optional[str]
        execution_history: Optional[list[ExecutionHistoryEntry]]
        investigation_id: Optional[str]
        last_modified_at: Optional[datetime]
        last_modified_by: Optional[str]
        last_modified_by_type: Optional[Union[str, ByType]]
        name: str
        parent_id: Optional[str]
        priority: Optional[Union[str, TaskPriority]]
        related_to: Optional[list[str]]
        status: Optional[Union[str, TaskStatus]]
        storage_asset_ids: Optional[list[str]]
        task_result: Optional[TaskResult]
        title: Optional[str]
        validation_requirements: Optional[list[str]]

        @overload
        def __init__(
                self, 
                *, 
                assigned_to: Optional[TaskAssignee] = ..., 
                comments: Optional[list[TaskComment]] = ..., 
                created_by_type: Optional[Union[str, ByType]] = ..., 
                depends_on: Optional[list[str]] = ..., 
                description: Optional[str] = ..., 
                investigation_id: Optional[str] = ..., 
                parent_id: Optional[str] = ..., 
                priority: Optional[Union[str, TaskPriority]] = ..., 
                related_to: Optional[list[str]] = ..., 
                status: Optional[Union[str, TaskStatus]] = ..., 
                storage_asset_ids: Optional[list[str]] = ..., 
                task_result: Optional[TaskResult] = ..., 
                title: Optional[str] = ..., 
                validation_requirements: Optional[list[str]] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.TaskAssignee(_Model):
        id: str
        type: Union[str, ByType]

        @overload
        def __init__(
                self, 
                *, 
                id: str, 
                type: Union[str, ByType]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.TaskComment(_Model):
        created_by: str
        created_by_type: Union[str, ByType]
        text: str
        timestamp: Optional[datetime]

        @overload
        def __init__(
                self, 
                *, 
                created_by: str, 
                created_by_type: Union[str, ByType], 
                text: str, 
                timestamp: Optional[datetime] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.TaskPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        HIGH = "High"
        LOW = "Low"
        MEDIUM = "Medium"


    class azure.ai.discovery.models.TaskResult(_Model):
        storage_asset_ids: Optional[list[str]]
        text: Optional[str]

        @overload
        def __init__(
                self, 
                *, 
                storage_asset_ids: Optional[list[str]] = ..., 
                text: Optional[str] = ...
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.TaskStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        COMPLETE = "Complete"
        EXECUTING = "Executing"
        EXECUTION_DONE = "ExecutionDone"
        FAILED = "Failed"
        FLAGGED_AI = "FlaggedAi"
        FLAGGED_HUMAN = "FlaggedHuman"
        INCOMPLETE = "Incomplete"
        NEW = "New"
        ON_HOLD = "OnHold"
        REMOVED = "Removed"
        STALE = "Stale"


    class azure.ai.discovery.models.WorkingMemoryEntry(_Model):
        content: str
        created_at: Optional[datetime]
        type: Union[str, WorkingMemoryEntryType]

        @overload
        def __init__(
                self, 
                *, 
                content: str, 
                type: Union[str, WorkingMemoryEntryType]
            ) -> None: ...

        @overload
        def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    class azure.ai.discovery.models.WorkingMemoryEntryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
        THOUGHT = "thought"


```