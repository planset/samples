package main

import (
	"errors"
	"fmt"
	"github.com/planset/gosample"
	"os"
)

func div(i, j int) (int, error) {
	if j == 0 {
		return 0, errors.New("divied by zero")
	}
	return i / j, nil
}

func hello() {
	fmt.Println("hello")
}

func sum(i int, j int) int {
	return i + j
}
func sum2(nums ...int) (result int) {
	for _, n := range nums {
		result += n
	}
	return
}

func swap(i int, j int) (int, int) {
	return j, i
}

func main() {
	fmt.Println(gosample.Message) // hello world

	var message1 string = "message1"
	fmt.Println(message1)

	message2 := "message2"
	fmt.Println(message2)

	var cnt int
	fmt.Println(cnt)

	if cnt == 0 {
		fmt.Println("true")
	} else if cnt == 1 {
		fmt.Println("1")
	} else {
		fmt.Println("else")
	}

	for i := 0; i < 3; i++ {
		if i == 2 {
			break
		}
		if i == 0 {
			continue
		}
		fmt.Println(i)
	}

	switch cnt {
	case 0:
		fmt.Println(0)
		fallthrough
	case 5, 10:
		fmt.Println("5,10")
	case 20:
		fmt.Println("5,10")
	default:
		fmt.Println("default")
	}
	switch {
	case cnt%3 == 0:
		fmt.Println("111")
	default:
		fmt.Println("222")
	}

	hello()

	n := sum(10, 20)
	fmt.Println(n)

	x, y := 1, 2
	x, y = swap(x, y)
	fmt.Println(x, y)

	_, err := os.Open("hello.go")
	if err != nil {
		fmt.Println("error:", err)
	}

	_, err2 := div(10, 0)
	if err2 != nil {
		fmt.Println(err2)
	}

	var s []string
	s = append(s, "a", "1", "2")
	s = append(s, gosample.Message)
	fmt.Println(s)
	fmt.Println(s[1:])

	for _i, _s := range s {
		fmt.Println(_i, _s)
	}

	fmt.Println(sum2(1, 2, 3, 4))

	var month map[int]string = map[int]string{}
	month[1] = "January"
	month[2] = "February"
	month[3] = "Hoge"
	delete(month, 3)

	for key, value := range month {
		fmt.Println(key, value)
	}

	var intVal int = 10
	callByRef(&intVal)
	fmt.Println(intVal)

	openFile()

	sampleProcessTask()

	sampleStruct()

}

func callByRef(i *int) {
	*i = 20
}

func openFile() {
	defer func() {
		err2 := recover()
		fmt.Println(err2)
		fmt.Println("defer")
	}()
	file, err := os.Open("hoge.go")
	if err != nil {
		panic(err)
	}
	defer file.Close()
}

type ID int
type Priority int

func ProcessTask(id ID, priority Priority) {
}

func sampleProcessTask() {
	var id ID = 3
	var priority Priority = 5
	ProcessTask(id, priority)
}

type Task struct {
	ID     int
	Detail string
	done   bool
}

func NewTask(id int, detail string) *Task {
	task := &Task{
		ID:     id,
		Detail: detail,
		done:   false,
	}
	return task
}

func sampleStruct() {
	task := NewTask(1, "buy the milk")
	fmt.Println(task.ID)
	fmt.Println(task.Detail)
	fmt.Println(task.done)

	task.Finish()
	Print(task)
}

func (task Task) String() string {
	doneString := " "
	if task.done {
		doneString = "*"
	}
	str := fmt.Sprintf("%s %d) %s", doneString, task.ID, task.Detail)
	return str
}
func (task *Task) Finish() {
	task.done = true
}

type Stringer interface {
	String() string
}

func Print(stringer Stringer) {
	fmt.Println(stringer.String())
}
